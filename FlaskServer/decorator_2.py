from flask import Flask

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

if __name__ == '__main__':
    app.run(debug=True)