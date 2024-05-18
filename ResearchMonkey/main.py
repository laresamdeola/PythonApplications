from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///researchmonkey.db"
# create extension
db = SQLAlchemy(model_class=Base)
# initialise app with the extension
db.init_app(app)


# create table
class ResearchPaper(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)


# create table schema in the database, requires application context
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    results = db.session.execute(db.select(ResearchPaper).order_by(ResearchPaper.author))
    all_research_papers = results.scalars().all()
    return render_template('index.html', papers=all_research_papers)


@app.route('/add', methods=['GET', 'POST'])
def add_paper():
    if request.method == 'POST':
        new_research_paper = ResearchPaper(
            title=request.form['paper-title'],
            author=request.form['paper-author']
        )
        db.session.add(new_research_paper)
        db.session.commit()
        print('Research Paper added successfully')
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)