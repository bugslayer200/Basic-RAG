import os
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH", "data/demo.pdf")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "pdf_chunks")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

_embed_model = None
VECTOR_SIZE = None


# ------------------------------
# Load Embedding Model
# ------------------------------

def load_model():
    global _embed_model, VECTOR_SIZE
    if _embed_model is None:
        from sentence_transformers import SentenceTransformer
        print(f"🔤 Loading embedding model: {EMBEDDING_MODEL}")
        _embed_model = SentenceTransformer(EMBEDDING_MODEL)
        VECTOR_SIZE = _embed_model.get_sentence_embedding_dimension()
    return _embed_model


def embed(text):
    model = load_model()
    vec = model.encode(text, convert_to_numpy=True)
    return np.asarray(vec, dtype=np.float32)


# ------------------------------
# PDF TEXT LOADER
# ------------------------------

def load_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text() or ""
        text += page_text + "\n"
    return text


# ------------------------------
# Simple Chunker
# ------------------------------

def chunk_text(text, chunk_size=500, chunk_overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - chunk_overlap
    return chunks


# ------------------------------
# Qdrant Connection
# ------------------------------

def connect_qdrant():
    print(f"🔌 Connecting to Qdrant at: {QDRANT_URL}")
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,  # Supports None for local
        timeout=30,
    )
    return client


def create_collection(client):
    if client.collection_exists(COLLECTION_NAME):
        print("ℹ️ Collection already exists, skipping creation.")
        return

    print(f"📚 Creating collection '{COLLECTION_NAME}'...")
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        ),
    )


def store_chunks(client, chunks):
    print(f"📥 Upserting {len(chunks)} chunks...")

    points = []
    for idx, chunk in enumerate(chunks):
        vec = embed(chunk).tolist()
        points.append(
            PointStruct(
                id=idx,
                vector=vec,
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


# ------------------------------
# Main Ingestion
# ------------------------------

def ingest():
    print("📄 Loading PDF...")
    text = load_pdf_text(PDF_PATH)

    print("✂️ Chunking PDF...")
    chunks = chunk_text(text)

    print("🔌 Connecting to Qdrant...")
    client = connect_qdrant()

    print("📚 Creating collection...")
    load_model()
    create_collection(client)

    print("📥 Storing chunks...")
    store_chunks(client, chunks)

    print(f"✅ Stored {len(chunks)} chunks in '{COLLECTION_NAME}'")
    return len(chunks)


if __name__ == "__main__":
    ingest()
