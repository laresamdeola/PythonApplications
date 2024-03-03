from flask import Flask
import time

app = Flask(__name__)

current_time = time.time()
#print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        begin_time = time.time()
        function()
        end_time = time.time()
        speed = end_time-begin_time
        print(f'{function.__name__} run speed: {speed}')
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()


if __name__=='__main__':
    app.run()