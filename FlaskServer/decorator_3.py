from flask import Flask


app = Flask(__name__)


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        # print(function(**kwargs))
        return f'You called {function.__name__}{args} \nIt returned {function(args[0], args[1], args[2])}'
    return wrapper

@logging_decorator
def a_function(a, b, c):
    return a * b * c

print(a_function(1, 2, 3))

if __name__ == '__main__':
    app.run(debug=True)