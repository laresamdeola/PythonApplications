# Building a Contact Form

from flask import Flask, render_template, url_for, request as req
# import random
# from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/login', methods=['POST'])
def login():
    name = req.form['name_input']
    password = req.form['password_input']
    return render_template('login.html', name=name, password=password)


if __name__ == '__main__':
    app.run(debug=True)