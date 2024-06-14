from flask import Flask, render_template, redirect, url_for, request, jsonify
import random
import math
from model import translate_model


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        text = request.form['english-text']
        translated_text = translate_model(text)
        print(translated_text)
        return render_template('translate.html', translated_text=translated_text)
    return render_template("translate.html", translated_text="")


if __name__ == "__main__":
    app.run(debug=True)


# To do
# 1. Link the pages.