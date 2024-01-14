from flask import Flask, jsonify, request

app = Flask(__name__)

# Books data
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 5, "title": "Brave New World", "author": "Aldous Huxley"},
]


# Get all books
@app.route('/', methods=['GET'])
def get_all_books():
    return jsonify({"books": books})

# Get a specific book by ID
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify({"book": book})
    return jsonify({"message": "Book not found"}), 404

# To add a new book
@app.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author")
    }
    books.append(new_book)
    return jsonify({"message": "Book added successfully", "book": new_book}), 201

# To delete a book by ID
@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": f"Book {book_id} deleted successfully"}), 200

# To update a book by ID
@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book['title'] = data.get("title", book['title'])
        book['author'] = data.get("author", book['author'])
        return jsonify({"message": f"Book {book_id} updated successfully", "book": book}), 200
    return jsonify({"message": "Book not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
