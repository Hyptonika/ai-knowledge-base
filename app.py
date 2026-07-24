from flask import Flask, request, render_template, redirect
from core.search import search
from core.ingest import load_text, chunk_text, embed_chunks
from core.models import create_table, save_chunk

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file and file.filename.endswith(".txt"):
        filepath = os.path.join("data", file.filename)
        file.save(filepath)

        text = load_text(filepath)
        chunks = chunk_text(text)
        embeddings = embed_chunks(chunks)

        for chunk, embedding in zip(chunks, embeddings):
            save_chunk(chunk, embedding)

    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        results = search(query)
    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")