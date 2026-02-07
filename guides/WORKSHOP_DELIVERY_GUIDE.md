# Workshop Delivery Guide - Full Day

## Morning Session (Kaggle) - status selesai
- 10.00-10.30: Notebook 01 (RAG fundamentals)
- 10.30-11.15: Notebook 02 (OCR quality)
- 11.15-12.00: Notebook 03 (chunking)

## Afternoon Session (Local MacBook) - 13.00-15.00

### 13.00-13.20 | Setup & validasi environment
**Tujuan:** semua peserta bisa menjalankan environment lokal.
- Cek `python --version`
- Cek `tesseract --version`
- Install dependency jika ada yang tertinggal.

### 13.20-13.50 | Bedah arsitektur production code
**Tujuan:** peserta memahami alur modular.
- `processor.py`: ingestion + quality scoring
- `chunker.py`: strategy chunking legal-aware
- `embedder.py`: model loading + embedding
- `retriever.py`: cosine top-k
- `pipeline.py`: orchestration

### 13.50-14.25 | Hands-on dengan dokumen riil
**Aktivitas:**
1. Peserta menaruh dokumen `.txt` pada `data/documents`.
2. Jalankan CLI:
   ```bash
   python production_code/main.py "Apa batas waktu tindak lanjut laporan?"
   ```
3. Interpretasi hasil score + chunk.

### 14.25-14.45 | Troubleshooting clinic
- Output tidak relevan -> cek kualitas OCR & chunk strategy.
- Runtime lambat -> model cache + kurangi top-k.
- Hasil terlalu pendek -> gunakan strategy `legal`.

### 14.45-15.00 | Deployment roadmap ke Komdigi
- Gunakan service wrapper (FastAPI) untuk endpoint query.
- Simpan index metadata di object storage.
- Tambah monitoring (latency, retrieval quality).
- Buat governance: versioning model, dokumen, dan prompt.

## Advanced Track (opsional)
- Re-ranking dengan cross-encoder.
- Evaluasi retrieval (MRR/Recall@K).
- Hybrid search (keyword + semantic).
