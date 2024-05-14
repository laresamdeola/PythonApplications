# Building a Contact Form

from flask import Flask, render_template, url_for, request as req
# import random
# from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/base')
def base_page():
    return render_template('base.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/success')
def success_page():
    return render_template('success.html')


@app.route('/denied')
def denied_page():
    return render_template('denied.html')


@app.route('/login', methods=['POST'])
def login():
    name = req.form['name_input']
    password = req.form['password_input']
    if name == 'admin@email.com' and password == '12345678':
        return render_template('success.html')
    else:
        return render_template('denied.html')
    # return render_template('login.html', name=name, password=password)


if __name__ == '__main__':
    app.run(debug=True)