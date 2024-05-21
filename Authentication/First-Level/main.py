from flask import Flask, render_template, redirect, url_for, request, send_from_directory, flash, get_flashed_messages
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from config import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
# create extension
db = SQLAlchemy(model_class=Base)
# initialise app with the extension
db.init_app(app)

# configure flask login's login manager
login_manager = LoginManager()
login_manager.init_app(app)


# create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# create table
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)


# create table schema in the database, requires application context
with app.app_context():
    db.create_all()
#
# global hash_and_salted_password


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        result_email = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if result_email:
            # user already exists
            flash("You've already signed up with that email, login instead")
            return redirect(url_for('login'))
        password = request.form['password']
        hash_and_salted_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        new_user = User(
            email=email,
            name=name,
            password=hash_and_salted_password
        )

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(url_for('secrets'))

    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        query_email = request.form['email']
        query_name = request.form['name']
        query_password = request.form['password']
        user = db.session.execute(db.select(User).where(User.email == query_email)).scalar()

        # email doesn't exist
        if not user:
            flash('That email does not exist, please try again')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, query_password):
            flash('Password incorrect, please try again')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    else:
        return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template('secrets.html', name=current_user.name)


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.txt')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)