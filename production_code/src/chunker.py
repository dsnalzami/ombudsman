"""Strategi chunking untuk dokumen legal Indonesia."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from .processor import Document


@dataclass
class Chunk:
    """Representasi chunk siap embedding."""

    chunk_id: str
    doc_id: str
    text: str
    strategy: str


class LegalChunker:
    """Chunker dengan mode fixed, sentence, dan legal-aware."""

    def chunk(self, documents: Iterable[Document], strategy: str = "legal", size: int = 1200) -> list[Chunk]:
        """Memecah dokumen menjadi chunk.

        Args:
            documents: Koleksi dokumen.
            strategy: fixed | sentence | legal.
            size: Parameter ukuran default.

        Returns:
            Daftar chunk.
        """

        chunks: list[Chunk] = []
        for doc in documents:
            if strategy == "fixed":
                segments = self._fixed_size(doc.content, size)
            elif strategy == "sentence":
                segments = self._sentence_based(doc.content, max_sentences=3)
            else:
                segments = self._legal_aware(doc.content)

            for idx, segment in enumerate(segments):
                chunks.append(
                    Chunk(
                        chunk_id=f"{doc.doc_id}_{strategy}_{idx:03d}",
                        doc_id=doc.doc_id,
                        text=segment,
                        strategy=strategy,
                    )
                )
        return chunks

    @staticmethod
    def _fixed_size(text: str, size: int) -> list[str]:
        return [text[i : i + size] for i in range(0, len(text), size)]

    @staticmethod
    def _sentence_based(text: str, max_sentences: int) -> list[str]:
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
        return [" ".join(sentences[i : i + max_sentences]) for i in range(0, len(sentences), max_sentences)]

    @staticmethod
    def _legal_aware(text: str) -> list[str]:
        pasal_pattern = re.compile(r"(?=\bPasal\s+\d+[A-Za-z]?)", re.IGNORECASE)
        candidates = [part.strip() for part in pasal_pattern.split(text) if part.strip()]
        if len(candidates) <= 1:
            return LegalChunker._sentence_based(text, max_sentences=4)
        return candidates
