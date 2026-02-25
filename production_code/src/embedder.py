"""Embedding service berbasis sentence-transformers."""

from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from .chunker import Chunk

logger = logging.getLogger(__name__)


class Embedder:
    """Wrapper model embedding untuk memudahkan dependency injection."""

    def __init__(self, model_name: str, cache_dir: Path) -> None:
        self.model_name = model_name
        self.cache_dir = cache_dir
        self._model: SentenceTransformer | None = None

    @property
    def model(self) -> SentenceTransformer:
        """Lazy-load model untuk menghemat startup time."""

        if self._model is None:
            logger.info("Memuat model embedding: %s", self.model_name)
            self._model = SentenceTransformer(self.model_name, cache_folder=str(self.cache_dir))
        return self._model

    def encode_chunks(self, chunks: list[Chunk]) -> np.ndarray:
        """Mengubah teks chunk menjadi vektor embedding."""

        texts = [chunk.text for chunk in chunks]
        vectors = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return vectors

    def encode_query(self, query: str) -> np.ndarray:
        """Mengubah query user menjadi vektor embedding."""

        return self.model.encode([query], convert_to_numpy=True, normalize_embeddings=True)[0]
