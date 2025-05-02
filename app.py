import json
import difflib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load the catalog from JSON
def load_catalog():
    with open('catalog.json') as f:
        return json.load(f)

# Fuzzy title match
def search_by_title(title_query):
    catalog = load_catalog()
    titles = [book['title'] for book in catalog]
    close_matches = difflib.get_close_matches(title_query, titles, n=1, cutoff=0.5)

    if close_matches:
        match = close_matches[0]
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

# Determine search type
def search_book(user_input):
    if "by" in user_input.lower():
        author_query = user_input.lower().split("by")[1].strip()
        return search_by_author(author_query)
    else:
        return search_by_title(user_input)

# Route for the chat interface
@app.route('/')
def index():
    return render_template('chat.html')

# Route for handling messages
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    response = search_book(user_input)
    return jsonify({"response": response})

# Run the app (Render-compatible)
if __name__ == '__main__':
    print("Launching chatbot website...")
    port = int(os.environ.get("PORT", 5000))  # <-- This is what Render needs
    app.run(host='0.0.0.0', port=port)
