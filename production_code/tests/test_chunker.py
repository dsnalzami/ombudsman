from pathlib import Path

from src.chunker import LegalChunker
from src.processor import Document


def test_legal_chunker_splits_on_pasal() -> None:
    doc = Document(
        doc_id="PER_TEST",
        source_path=Path("PER_TEST.txt"),
        content="Pasal 1 Ketentuan umum. Pasal 2 Hak pelapor. Pasal 3 Penutup.",
        quality_score=0.9,
    )
    chunks = LegalChunker().chunk([doc], strategy="legal")
    assert len(chunks) == 3
    assert chunks[0].text.startswith("Pasal 1")
