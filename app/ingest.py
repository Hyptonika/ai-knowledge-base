from sentence_transformers import SentenceTransformer
from app.models import create_table, save_chunk

model = SentenceTransformer('all-MiniLM-L6-v2')

def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    return embeddings

if __name__ == "__main__":
    create_table()

    text = load_text("data/notes.txt")
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    for chunk, embedding in zip(chunks, embeddings):
        save_chunk(chunk, embedding)

    print(f"Saved {len(chunks)} chunks to the database.")