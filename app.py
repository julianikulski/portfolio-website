from flask import Flask, jsonify, session, render_template, request, Response, redirect, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import helper
import os

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = helper.get_title_content('index')

    return render_template('/index.html',
                            title_text=title_text,
                            title="DATA SCIENCE & SUSTAINABILITY",
                            id="index")

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # get all projects from the database
    project_list = helper.get_portfolio_content()

    # create list of lists that contains pairs of projects
    if len(project_list) % 2 == 0:
        pass
    else:
        project_list.append(['placeholder'])
    iterator = iter(project_list)
    zipped = zip(iterator, iterator)

    # get the title content for the portfolio page
    title_text = helper.get_title_content('portfolio')

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJEKTPORTFOLIO",
                            id="portfolio",
                            projects=zipped)

@app.route('/about', methods=['POST', 'GET'])
def about():

    title_text = helper.get_title_content('about')

    path = ["Während meines Bachelorstudiums: Verschiedene Forschungsprojekte mit R",
            "Januar bis November 2018: CS50's Introduction to Computer Science",
            "Januar bis August 2019: Udacity's Data Scientist Nanodegree",
            "Oktober 2019 bis Februar 2020: Data Science Seminar im Rahmen meines \
            Masterstudiengangs"]

    skills = helper.get_skill_content()

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ÜBER MICH",
                            id="about")

@app.route('/impressum', methods=['POST', 'GET'])
def impressum():

    try:
        import config
        address_one = config.address_one
        address_two = config.address_two
        email = config.email

    except:
        address_one = os.environ['ADDRESS_ONE']
        address_two = os.environ['ADDRESS_TWO']
        email = os.environ['EMAIL']

    return render_template('/impressum.html',
                            title="IMPRESSUM",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index")

@app.route('/datenschutz', methods=['POST', 'GET'])
def datenschutz():

    try:
        import config
        address_one = config.address_one
        address_two = config.address_two
        email = config.email

    except:
        address_one = os.environ['ADDRESS_ONE']
        address_two = os.environ['ADDRESS_TWO']
        email = os.environ['EMAIL']

    return render_template('/datenschutz.html',
                            title="DATENSCHUTZ",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index")


@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])
