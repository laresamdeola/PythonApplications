from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
# create extension
db = SQLAlchemy(model_class=Base)
# initialise app with the extension
db.init_app(app)


# create table
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)


# create table schema in the database, requires application context
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(
            email=email,
            name=name,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        query_email = request.form['email']
        query_name = request.form['name']
        query_password = request.form['password']
        result_email = db.session.execute(db.select(User).where(User.email == query_email)).scalar()
        result_password = db.session.execute(db.select(User).where(User.password == query_password)).scalar()
        if result_email and result_password:
            return render_template('secrets.html', name=query_name)
        else:
            return render_template('register.html')
    else:
        return render_template('login.html')


@app.route('/secrets')
def secrets():
    return render_template('secrets.html')


if __name__ == '__main__':
    app.run(debug=True)