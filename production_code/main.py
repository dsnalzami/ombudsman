"""CLI entry point pipeline RAG Ombudsman."""

from __future__ import annotations

import argparse
import json
import logging

from config.settings import DEFAULT_SETTINGS, ensure_directories
from src.pipeline import OmbudsmanRAGPipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RAG pipeline untuk dokumen Ombudsman")
    parser.add_argument("query", type=str, help="Pertanyaan pengguna")
    parser.add_argument("--strategy", default="legal", choices=["fixed", "sentence", "legal"])
    parser.add_argument("--quality-threshold", type=float, default=0.7)
    parser.add_argument("--top-k", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    args = parse_args()

    ensure_directories(DEFAULT_SETTINGS)
    pipeline = OmbudsmanRAGPipeline(DEFAULT_SETTINGS)
    retriever = pipeline.build_index(strategy=args.strategy, quality_threshold=args.quality_threshold)
    results = pipeline.answer(retriever, query=args.query, top_k=args.top_k)
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
