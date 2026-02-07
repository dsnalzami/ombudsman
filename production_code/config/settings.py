"""Konfigurasi utama untuk pipeline RAG Ombudsman."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Menyimpan seluruh konfigurasi runtime pipeline.

    Attributes:
        data_dir: Direktori berisi dokumen sumber (.txt/.pdf).
        cache_dir: Direktori cache model embedding.
        output_dir: Direktori output hasil indexing/retrieval.
        embedding_model: Nama model sentence-transformers.
        max_chunk_chars: Ukuran karakter maksimal per chunk fallback.
        top_k: Jumlah hasil retrieval yang dikembalikan.
    """

    data_dir: Path
    cache_dir: Path
    output_dir: Path
    embedding_model: str
    max_chunk_chars: int
    top_k: int


DEFAULT_SETTINGS = Settings(
    data_dir=Path(os.getenv("OMB_DATA_DIR", "data/documents")),
    cache_dir=Path(os.getenv("OMB_CACHE_DIR", "data/model_cache")),
    output_dir=Path(os.getenv("OMB_OUTPUT_DIR", "data/output")),
    embedding_model=os.getenv(
        "OMB_EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    ),
    max_chunk_chars=int(os.getenv("OMB_MAX_CHUNK_CHARS", "1200")),
    top_k=int(os.getenv("OMB_TOP_K", "5")),
)


def ensure_directories(settings: Settings = DEFAULT_SETTINGS) -> None:
    """Membuat direktori penting bila belum ada.

    Args:
        settings: Konfigurasi yang aktif.
    """

    for directory in [settings.data_dir, settings.cache_dir, settings.output_dir]:
        directory.mkdir(parents=True, exist_ok=True)
