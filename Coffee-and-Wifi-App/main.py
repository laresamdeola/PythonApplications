from flask import Flask, render_template, url_for, request, redirect
import pandas as pd
import csv


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as data:
        csv_reader = csv.DictReader(data)
        data = [row for row in csv_reader]
        fieldnames = csv_reader.fieldnames
    return render_template('cafes.html', data=data, fieldnames=fieldnames)


@app.route('/add', methods=['POST'])
def add():
    cafe_name = request.form['cafename']
    location = request.form['location']
    open_time = request.form['open']
    close_time = request.form['close']
    coffee = request.form['coffee']
    wifi = request.form['wifi']
    power = request.form['power']

    if cafe_name:
        with open('cafe-data.csv', mode='a', newline='') as data:
            writer = csv.writer(data)
            writer.writerow([cafe_name, location, open_time, close_time, coffee, wifi, power])
            return render_template('success.html')
    return render_template('form.html')


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/form')
def cafe_form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)