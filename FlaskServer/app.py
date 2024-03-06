from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function


def text_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function


def text_underline(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route('/')
@make_bold
@text_emphasis
@text_underline
def home():
    return 'Hello World!'


@app.route('/username/<year>')
def happy_new_year(year):
    return f'Welcome to year {year} number'


if __name__=='__main__':
    app.run(debug=True)
