from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
# create extension
db = SQLAlchemy(model_class=Base)
# initialise app with the extension
db.init_app(app)


# create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# create table schema in the database, requires application context
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # get all books
    result = db.session.execute(db.select(Book).order_by(Book.author))
    all_books = result.scalars().all()
    return render_template('index.html', books=all_books)


# add a new book
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(
            title=request.form['book-name'],
            author=request.form['book-author'],
            rating=request.form['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        print('Book added successfully')
        return redirect(url_for('home'))
    return render_template('add-book-form.html')


# update the rating record

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    books_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=books_selected)


# delete a specific book
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    print('Book has been deleted')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)