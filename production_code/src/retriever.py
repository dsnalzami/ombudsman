"""Retriever sederhana menggunakan cosine similarity."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .chunker import Chunk


@dataclass
class RetrievalResult:
    """Hasil retrieval untuk satu chunk."""

    chunk: Chunk
    score: float


class Retriever:
    """Komponen pencarian top-k dengan cosine similarity."""

    def __init__(self, chunks: list[Chunk], vectors: np.ndarray) -> None:
        if len(chunks) != len(vectors):
            raise ValueError("Jumlah chunk dan vector harus sama")
        self.chunks = chunks
        self.vectors = vectors

    def search(self, query_vector: np.ndarray, top_k: int = 5) -> list[RetrievalResult]:
        """Mencari chunk terdekat dari query.

        Args:
            query_vector: Embedding query.
            top_k: Jumlah hasil.

        Returns:
            Daftar hasil retrieval berurutan dari skor tertinggi.
        """

        similarity = self.vectors @ query_vector
        top_idx = np.argsort(similarity)[::-1][:top_k]
        return [RetrievalResult(chunk=self.chunks[i], score=float(similarity[i])) for i in top_idx]
