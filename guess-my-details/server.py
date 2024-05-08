from flask import Flask, render_template, url_for
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/guess/<name>')
def guess_page(name):

    # Guess the age through the name
    url_agify = f'https://api.agify.io?name={name}'
    response_age = requests.get(url_agify)
    data_age = response_age.json()
    age = data_age['age']

    # Guess the gender through the name
    url_genderize = f'https://api.genderize.io?name={name}'
    response_gender = requests.get(url_genderize)
    data_gender = response_gender.json()
    gender = data_gender['gender']

    # Guess the nationality through the name
    url_nationality = f'https://api.nationalize.io?name={name}'
    response_nationality = requests.get(url_nationality)
    data_nationality = response_nationality.json()
    nationality = data_nationality['country'][0]['country_id']

    # Need another API to fetch the full country name via country codes
    url_country_name = f'https://api.first.org/data/v1/countries?q={nationality}'
    response_country_name = requests.get(url_country_name)
    data_country_name = response_country_name.json()
    country = data_country_name['data'][nationality]['country']

    return render_template('index.html',
                           age=age,
                           gender=gender,
                           name=name,
                           nationality=nationality,
                           country=country)


@app.route('/blogposts')
def blog():
    url_blog_posts = "https://api.npoint.io/8c5f2341aec59a6b5852"
    response_blog_post = requests.get(url_blog_posts)
    print(response_blog_post)
    posts = response_blog_post.json()
    color = 'black'
    return render_template('blog.html', posts=posts, color=color)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)