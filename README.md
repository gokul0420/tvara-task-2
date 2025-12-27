## Summary
Implemented a minimal but correct RAG pipeline using FAISS and e5-small-v2 embeddings.
The pipeline converts a PDF into text chunks, embeds them, stores them in FAISS IndexFlatL2, and retrieves the top-k relevant chunks for a given query.

## Tech
- Python
- pypdf
- sentence-transformers (intfloat/e5-small-v2)
- FAISS

## Flow
PDF → Text Extract → Chunking → Embedding → FAISS → Retrieval

## Error Handling (Required)
- Empty query
- Empty PDF
- Corrupt PDF
- No chunks returned

## How To Run
pip install -r requirements.txt
python -m src.main

## Output
Returns top 2–3 chunks and similarity scores.

## Notes
This solution is intentionally lightweight but follows clean modular architecture.
