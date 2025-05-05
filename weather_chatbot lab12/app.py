from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = Flask(__name__)

# Load knowledge base
with open("weather_facts.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate document embeddings
doc_embeddings = model.encode(documents)

# Create FAISS index
index = faiss.IndexFlatL2(len(doc_embeddings[0]))
index.add(np.array(doc_embeddings))

@app.route('/')
def home():
    return '''
    <html>
      <head><title>Weather QnA Bot</title></head>
      <body style="font-family:sans-serif; padding:20px;">
        <h1>Ask a Weather Question</h1>
        <form method="POST" action="/get_answer">
          <input type="text" name="question" placeholder="E.g. How do tornadoes form?" size="50" required>
          <input type="submit" value="Ask">
        </form>
      </body>
    </html>
    '''

@app.route('/get_answer', methods=['POST'])
def get_answer():
    query = request.form['question']
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    answer = documents[I[0][0]]
    return f"<h2>Answer:</h2><p>{answer}</p><br><a href='/'>Ask Another Question</a>"

if __name__ == '__main__':
    app.run(debug=True)

