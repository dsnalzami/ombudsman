"""Modul pemrosesan dokumen untuk pipeline RAG."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)


@dataclass
class Document:
    """Representasi dokumen teks.

    Attributes:
        doc_id: ID unik dokumen.
        source_path: Path asli dokumen.
        content: Isi teks dokumen.
        quality_score: Skor kualitas sederhana (0-1).
    """

    doc_id: str
    source_path: Path
    content: str
    quality_score: float


class DocumentProcessor:
    """Mengambil, membaca, dan menilai kualitas dokumen teks."""

    def __init__(self, min_length: int = 80) -> None:
        self.min_length = min_length

    def load_txt_documents(self, input_dir: Path) -> list[Document]:
        """Membaca semua file .txt dalam sebuah folder.

        Args:
            input_dir: Folder dokumen sumber.

        Returns:
            Daftar dokumen yang lolos validasi minimal.
        """

        documents: list[Document] = []
        for path in sorted(input_dir.glob("*.txt")):
            try:
                raw_text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                logger.warning("Encoding UTF-8 gagal untuk %s, fallback latin-1", path)
                raw_text = path.read_text(encoding="latin-1")

            cleaned = self.preprocess_text(raw_text)
            score = self.assess_quality(cleaned)
            if len(cleaned) < self.min_length:
                logger.info("Lewati dokumen pendek: %s", path.name)
                continue

            documents.append(
                Document(doc_id=path.stem, source_path=path, content=cleaned, quality_score=score)
            )
        logger.info("Loaded %d dokumen dari %s", len(documents), input_dir)
        return documents

    @staticmethod
    def preprocess_text(text: str) -> str:
        """Pembersihan teks dasar pasca-OCR.

        Args:
            text: Teks mentah.

        Returns:
            Teks yang sudah dinormalisasi spasi.
        """

        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return "\n".join(lines)

    @staticmethod
    def assess_quality(text: str) -> float:
        """Menghitung skor kualitas sederhana berbasis heuristik.

        Args:
            text: Teks yang sudah dipreproses.

        Returns:
            Nilai 0-1 (semakin besar semakin baik).
        """

        if not text:
            return 0.0

        char_count = len(text)
        alpha_ratio = sum(c.isalpha() or c.isspace() for c in text) / char_count
        weird_ratio = sum(c in "@#$%^&*<>|~`" for c in text) / char_count
        return max(0.0, min(1.0, alpha_ratio - weird_ratio))


def filter_by_quality(documents: Iterable[Document], threshold: float = 0.7) -> list[Document]:
    """Memilih dokumen dengan skor kualitas tertentu."""

    return [doc for doc in documents if doc.quality_score >= threshold]
