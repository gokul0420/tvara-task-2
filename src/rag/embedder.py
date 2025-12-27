import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

model=SentenceTransformer("intfloat/e5-small-v2")

def build_index(chunks):
    embeddings=model.encode(chunks)
    embeddings=np.array(embeddings).astype("float32")
    index=faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index