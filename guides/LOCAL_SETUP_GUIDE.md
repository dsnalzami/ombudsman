# Local Setup Guide (MacBook M4 Pro) - Part B

## 1) Install dasar
1. Install Homebrew (jika belum ada).
2. Install Anaconda/Miniconda.
3. Install Tesseract:
   ```bash
   brew install tesseract tesseract-lang
   ```
4. Validasi:
   ```bash
   tesseract --version
   ```

## 2) Buat environment Python
```bash
conda create -n ombudsman-rag python=3.11 -y
conda activate ombudsman-rag
pip install -r production_code/requirements.txt
```

## 3) Struktur data lokal
Simpan dokumen `.txt` di folder `data/documents` atau ubah via environment variable:
```bash
export OMB_DATA_DIR=/path/ke/dokumen
export OMB_CACHE_DIR=$HOME/.cache/ombudsman-rag
export OMB_OUTPUT_DIR=./data/output
```

## 4) Warm-up model (opsional, direkomendasikan)
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2')"
```

## 5) Menjalankan pipeline
```bash
python production_code/main.py "Bagaimana prosedur pengaduan masyarakat?" --strategy legal --top-k 5
```

## 6) Troubleshooting cepat
- Jika model lambat pertama kali: normal karena download cache.
- Jika OCR jelek: jalankan preprocessing scan dulu (deskew + denoise).
- Jika memory tinggi: gunakan chunk strategy `sentence` + kurangi `--top-k`.
