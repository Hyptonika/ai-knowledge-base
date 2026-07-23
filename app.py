from flask import Flask, request, render_template
from app.search import search

app = Flask(__name__)

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