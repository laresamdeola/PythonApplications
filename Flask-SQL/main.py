from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import csv


app = Flask(__name__)


all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add')
def add_book_form():
    return render_template('add-book-form.html')


@app.route('/add', methods=['POST'])
def add_book():
    book_name = request.form['book-name']
    book_author = request.form['book-author']
    book_rating = request.form['rating']
    book_details = {
        'title': book_name or '',
        'author': book_author or '',
        'rating': book_rating or ''
    }

    if book_name and book_author and book_rating:
        all_books.append(book_details)
        return render_template('index.html', book_details=all_books)
    return render_template('add-book-form.html')


if __name__ == '__main__':
    app.run(debug=True)