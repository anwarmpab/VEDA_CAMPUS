import json
import os

DATA_PATH = os.path.join("data", "books.json")

def search_library(query):
    try:
        if not os.path.exists(DATA_PATH):
            return "Library data not found."

        with open(DATA_PATH, "r") as file:
            books = json.load(file)

        keywords = query.lower().split()
        matches = []

        for book in books:
            book_topics = " ".join(book["topics"]).lower()
            if any(word in book_topics for word in keywords):
                info = f"📘 {book['title']} by {book['author']}\n  • QR Code: {book['qr']}\n  • Rack: {book['rack']}\n  • Topics: {', '.join(book['topics'])}"
                matches.append(info)

        if matches:
            return "\n\n".join(matches)
        else:
            return "No relevant books found for that topic."

    except Exception as e:
        return f"Error searching library: {str(e)}"
def search_books(query):
    return "📚 Library search is coming soon! I’ll help you find books by topic or subject."
