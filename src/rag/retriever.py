import numpy as np 
from .embedder import model

def search(index,chunks,query:str,k:int=3):
    if not query.strip():
        raise ValueError("Query is empty")

    q=model.encode([query]).astype("float32")
    distances,indices=index.search(q,k)
    result=[chunks[i] for i in indices[0]]
    scores=distances[0].tolist()
    return{
        "chunks":result,
        "scores":scores
    }