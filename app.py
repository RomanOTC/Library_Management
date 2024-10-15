from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/library_db"  # Update this URI if needed
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        publication_year = request.form.get('publication_year')

        # Insert into MongoDB
        mongo.db.books.insert_one({
            'title': title,
            'author': author,
            'genre': genre,
            'publication_year': publication_year
        })
        return redirect(url_for('view_books'))
    
    return render_template('add_book.html')

@app.route('/view_books')
def view_books():
    books = mongo.db.books.find()
    return render_template('view_books.html', books=books)

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})
    return redirect(url_for('view_books'))

@app.route('/search_book', methods=['GET', 'POST'])
def search_book():
    if request.method == 'POST':
        title = request.form.get('title')
        books = mongo.db.books.find({"title": {"$regex": title, "$options": "i"}})  # Case-insensitive search
        return render_template('search_book.html', books=books, search_title=title)
    
    return render_template('search_book.html', books=None)

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # You can change the port if needed
