from sentence_transformers import SentenceTransformer

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
    text = load_text("data/notes.txt")
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    print(f"Total chunks: {len(chunks)}")
    print(f"Embedding shape: {embeddings.shape}")