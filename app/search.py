import numpy as np
from app.models import get_all_chunks
from app.ingest import model

def bytes_to_embedding(blob):
    return np.frombuffer(blob, dtype=np.float32)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, top_k=2):
    query_embedding = model.encode([query])[0]

    rows = get_all_chunks()
    results = []

    for row_id, text, embedding_blob in rows:
        chunk_embedding = bytes_to_embedding(embedding_blob)
        score = cosine_similarity(query_embedding, chunk_embedding)
        results.append((score, text))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_k]

if __name__ == "__main__":
    query = "your test question here"
    results = search(query)
    for score, text in results:
        print(f"Score: {score:.3f} — {text[:60]}")