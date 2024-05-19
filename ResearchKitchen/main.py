from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.sql.functions import func
import random
import math


app = Flask(__name__)


# Create Database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///researchkitchen.db"
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


@app.route('/delete')
def delete_paper():
    paper_id = request.args.get('id')
    paper_to_delete = db.get_or_404(ResearchPaper, paper_id)
    db.session.delete(paper_to_delete)
    db.session.commit()
    print(f'{paper_id} has been deleted')
    return redirect(url_for('home'))


# ResearchKitchen API

# API route to get a random paper
@app.route('/random')
def random_paper():
    my_query = db.func.count(ResearchPaper.id)
    count = db.session.execute(my_query).scalar()
    random_number = random.randint(1, count)
    paper_result = db.session.execute(db.select(
        ResearchPaper).where(ResearchPaper.id == random_number)).scalar()
    # print(paper_result.title)
    # return a json object
    return jsonify(
        id=paper_result.id,
        title=paper_result.title,
        author=paper_result.author
    )


@app.route('/all-papers')
def get_all_papers():
    result = db.session.execute(db.select(ResearchPaper).order_by(ResearchPaper.title))
    all_papers = result.scalars()
    papers = []
    for paper in all_papers:
        paper_dict = {
            'id': paper.id,
            'title': paper.title,
            'author': paper.author
        }
        papers.append(paper_dict)
    return jsonify(papers)


# find a research paper
@app.route('/search-paper')
def search_paper():
    search_query = request.args.get('title')
    papers = db.session.execute(db.select(ResearchPaper).where(ResearchPaper.title == search_query)).scalars().all()
    found_paper = []
    for paper in papers:
        paper_dict = {
            'id': paper.id,
            'title': paper.title,
            'author': paper.author
        }
        found_paper.append(paper_dict)
    if papers:
        return jsonify(found_paper)
    else:
        return jsonify(
            error={"Not found": "The paper is not in the database yet"}
        ), 404


# update - patch the research paper title
@app.route("/update-title/<int:paper_id>", methods=["PATCH", "GET"])
def update_paper_title(paper_id):
    new_title = request.args.get('new_title')
    paper = db.get_or_404(ResearchPaper, paper_id)
    print(paper)
    if paper:
        paper.title = new_title
        db.session.commit()
        return jsonify(response={'success': 'Successfully updated the research paper title'})
    else:
        return jsonify(response={'Unable to change': 'You cannot change the title of the research paper'})


# delete route
@app.route("/delete-paper/<int:paper_id>", methods=["DELETE", "GET"])
def delete_research_paper(paper_id):
    api_key = request.args.get('api_key')
    if api_key == 'GOOD':
        paper = db.get_or_404(ResearchPaper, paper_id)
        if paper:
            db.session.delete(paper)
            db.session.commit()
            return jsonify(response={'success': 'Research Paper has been deleted.'}), 200
        else:
            return jsonify(error={'Not Found': 'The research paper cannot be found'}), 404
    else:
        return jsonify(error={'Forbidden': 'You are not authorised.'}), 403


if __name__ == "__main__":
    app.run(debug=True)