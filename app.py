import json
import difflib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load book catalog
def load_catalog():
    with open('catalog.json') as f:
        return json.load(f)

# Fuzzy title search
def search_by_title(title_query):
    catalog = load_catalog()
    titles = [book['title'] for book in catalog]
    matches = difflib.get_close_matches(title_query, titles, n=1, cutoff=0.5)

    if matches:
        match = matches[0]
        for book in catalog:
            if book['title'] == match:
                status = "available" if book['available'] else "not available"
                return f"'{book['title']}' by {book['author']}' is located at {book['location']} and is currently {status}."
    return "Sorry, I couldn't find that book in the catalog."

# Author search
def search_by_author(author_query):
    catalog = load_catalog()
    results = []

    for book in catalog:
        if author_query.lower() in book['author'].lower():
            status = "available" if book['available'] else "not available"
            results.append(f"'{book['title']}' (Shelf: {book['location']}, {status})")

    if results:
        return f"Books by {author_query}:\n" + "\n".join(results)
    else:
        return f"Sorry, I couldn't find any books by {author_query}."

# Genre search
def search_by_genre(genre_query):
    catalog = load_catalog()
    results = []

    for book in catalog:
        if genre_query.lower() == book.get('genre', '').lower():
            status = "available" if book['available'] else "not available"
            results.append(f"'{book['title']}' by {book['author']} ({status}, Shelf: {book['location']})")

    if results:
        return f"Books in the '{genre_query}' genre:\n" + "\n".join(results)
    else:
        return f"Sorry, I couldn't find any books in the '{genre_query}' genre."

# Decide how to respond
def search_book(user_input):
    user_input = user_input.lower()

    # Check for genre
    genres = ["fiction", "history", "science", "poetry", "technology", "religion"]
    for genre in genres:
        if genre in user_input:
            return search_by_genre(genre)

    # Check for author
    if "by" in user_input:
        author_query = user_input.split("by")[1].strip()
        return search_by_author(author_query)

    # Default to title
    return search_by_title(user_input)

# Serve frontend
@app.route('/')
def index():
    return render_template('chat.html')

# Handle chatbot POST
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = search_book(user_input)
    return jsonify({"response": response})

# Launch server
if __name__ == '__main__':
    print("Launching chatbot website...")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
