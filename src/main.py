from src.rag.loader import load_pdf
from src.rag.chunker import chunk_text
from src.rag.embedder import build_index
from src.rag.retriever import search

def run_rag(pdf_path:str,query:str):
    print("RAG PIPELINE DEMO")
    text=load_pdf(pdf_path)
    chunks=chunk_text(text)
    if not chunks:
        raise ValueError("No chunks")
    index=build_index(chunks)
    results=search(index,chunks,query=query,k=3)
    print("top retrieved chunks")
    for i,c in enumerate(results["chunks"]):
        print(f"[{i+1}] {c[:200]}...\n")
    print("Scores:",results["scores"])

if __name__ == "__main__":
    run_rag("pdf/sample.pdf","What are the risks of machine learning?")