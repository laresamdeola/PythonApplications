from flask import Flask, render_template, url_for
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home_page():
    random_number = random.randint(1, 100)
    copyright_year = datetime.now().year
    author = 'Lare'
    return render_template('index.html',
                           random_number=random_number,
                           copyright_year=copyright_year,
                           author=author)


if __name__ == '__main__':
    app.run(debug=True)