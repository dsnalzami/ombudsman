"""Orkestrasi end-to-end RAG pipeline."""

from __future__ import annotations

import json
import logging
from dataclasses import asdict
from pathlib import Path

from config.settings import Settings

from .chunker import LegalChunker
from .embedder import Embedder
from .processor import DocumentProcessor, filter_by_quality
from .retriever import Retriever

logger = logging.getLogger(__name__)


class OmbudsmanRAGPipeline:
    """Pipeline utama untuk indexing dan retrieval dokumen legal."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.processor = DocumentProcessor()
        self.chunker = LegalChunker()
        self.embedder = Embedder(settings.embedding_model, settings.cache_dir)

    def build_index(self, strategy: str = "legal", quality_threshold: float = 0.7) -> Retriever:
        """Membangun retriever dari dokumen sumber."""

        documents = self.processor.load_txt_documents(self.settings.data_dir)
        good_docs = filter_by_quality(documents, threshold=quality_threshold)
        logger.info("Dokumen lolos quality threshold: %d/%d", len(good_docs), len(documents))

        chunks = self.chunker.chunk(good_docs, strategy=strategy, size=self.settings.max_chunk_chars)
        vectors = self.embedder.encode_chunks(chunks)
        self._save_index_metadata(chunks)
        return Retriever(chunks, vectors)

    def answer(self, retriever: Retriever, query: str, top_k: int | None = None) -> list[dict]:
        """Menjalankan retrieval untuk query.

        Returns:
            List dictionary agar mudah di-serialize ke JSON.
        """

        k = top_k or self.settings.top_k
        query_vector = self.embedder.encode_query(query)
        results = retriever.search(query_vector, top_k=k)
        return [
            {
                "doc_id": item.chunk.doc_id,
                "chunk_id": item.chunk.chunk_id,
                "score": round(item.score, 4),
                "text": item.chunk.text[:300],
            }
            for item in results
        ]

    def _save_index_metadata(self, chunks: list) -> None:
        """Menyimpan metadata chunk untuk audit/troubleshooting."""

        metadata_file = Path(self.settings.output_dir) / "index_metadata.json"
        serializable = [asdict(chunk) for chunk in chunks]
        metadata_file.write_text(json.dumps(serializable, ensure_ascii=False, indent=2), encoding="utf-8")
