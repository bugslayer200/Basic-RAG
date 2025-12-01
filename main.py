import os
import numpy as np
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "pdf_chunks")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

_embed_model = None

def load_model():
    global _embed_model
    if _embed_model is None:
        _embed_model = SentenceTransformer(EMBEDDING_MODEL, device='cpu')
    return _embed_model


def embed(text):
    m = load_model()
    v = m.encode(text, normalize_embeddings=True)
    return np.asarray(v, dtype=np.float32)


def run_query(query, k=5):
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    qvec = embed(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=qvec,            
        limit=k,
        with_payload=True      
    )

    return results

if __name__ == "__main__":
    q = input("Enter query: ")
    hits = run_query(q)
    for point in hits.points:
        print("Score:", point.score)
        print("Text:", point.payload.get("text", ""))
        print("-----")
