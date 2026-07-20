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

if __name__ == "__main__":
    text = load_text("data/notes.txt")
    chunks = chunk_text(text)
    print(f"Total chunks: {len(chunks)}")
    print(chunks[0])