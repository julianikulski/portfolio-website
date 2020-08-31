from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import helper
import os

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    # default language for my website
    lang = 'en'

    return redirect(url_for('index_en',
                                 lang=lang))


@app.route('/en/index', methods=['POST', 'GET'])
@app.route('/en/', methods=['POST', 'GET'])
def index_en(lang=None):

    # this happens if the language buttons are clicked
    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('index_de',
                                 lang=lang))
    # this happens if a GET request is sent
    else:
        lang = 'en'

    title_text = helper.get_title_content('index', lang)

    return render_template('index.html',
                                title_text=title_text,
                                title="DATA SCIENCE & SUSTAINABILITY",
                                id="index",
                                lang=lang)


@app.route('/de/index', methods=['POST', 'GET'])
@app.route('/de/', methods=['POST', 'GET'])
def index_de(lang=None):

    # this happens if the language buttons are clicked
    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('index_en',
                                 lang=lang))
    # this happens if a GET request is sent
    else:
        lang = 'de'

    title_text = helper.get_title_content('index', lang)

    return render_template('index.html',
                                title_text=title_text,
                                title="DATA SCIENCE & SUSTAINABILITY",
                                id="index",
                                lang=lang)


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    # default language if just portfolio is entered in url
    lang = 'en'

    return redirect(url_for('portfolio_en',
                                 lang=lang))


@app.route('/en/portfolio', methods=['POST', 'GET'])
def portfolio_en():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('portfolio_de',
                                 lang=lang))
    else:
        lang = 'en'

    # get all projects from the database
    zipped = helper.get_portfolio_content(lang)

    # get the title content for the portfolio page
    title_text = helper.get_title_content('portfolio', lang)

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJECT PORTFOLIO",
                            id="portfolio",
                            projects=zipped,
                            lang=lang)


@app.route('/de/portfolio', methods=['POST', 'GET'])
def portfolio_de():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('portfolio_en',
                                 lang=lang))
    else:
        lang = 'de'

    # get all projects from the database
    zipped = helper.get_portfolio_content(lang)

    # get the title content for the portfolio page
    title_text = helper.get_title_content('portfolio', lang)

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJEKTPORTFOLIO",
                            id="portfolio",
                            projects=zipped,
                            lang=lang)


@app.route('/about', methods=['POST', 'GET'])
def about():

    # default language if user enters about without language preference in url
    lang = 'en'

    return redirect(url_for('about_en',
                             lang=lang))


@app.route('/en/about', methods=['POST', 'GET'])
def about_en():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('about_de',
                                 lang=lang))
    else:
        lang = 'en'

    title_text = helper.get_title_content('about', lang)

    skills = helper.get_skill_content(lang)

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ABOUT ME",
                            id="about",
                            lang=lang)


@app.route('/de/about', methods=['POST', 'GET'])
def about_de():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('about_en',
                                 lang=lang))
    else:
        lang = 'de'

    title_text = helper.get_title_content('about', lang)

    skills = helper.get_skill_content(lang)

    return render_template('/about.html',
                            title_text=title_text,
                            skills=skills,
                            title="ÜBER MICH",
                            id="about",
                            lang=lang)


@app.route('/impressum', methods=['POST', 'GET'])
def impressum():

    lang = 'en'

    return redirect(url_for('impressum_en',
                             lang=lang))


@app.route('/en/impressum', methods=['POST', 'GET'])
def impressum_en():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('impressum_de',
                                 lang=lang))
    else:
        lang = 'en'

    address_one, address_two, email = helper.get_privacy_legal_notice()

    return render_template('/impressum.html',
                            title="LEGAL NOTICE (ONLY AVAILABLE IN GERMAN)",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index",
                            lang=lang)


@app.route('/de/impressum', methods=['POST', 'GET'])
def impressum_de():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('impressum_en',
                                 lang=lang))
    else:
        lang = 'de'

    address_one, address_two, email = helper.get_privacy_legal_notice()

    return render_template('/impressum.html',
                            title="IMPRESSUM",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index",
                            lang=lang)


@app.route('/datenschutz', methods=['POST', 'GET'])
def datenschutz():

    lang = 'en'

    return redirect(url_for('datenschutz_en',
                             lang=lang))


@app.route('/en/datenschutz', methods=['POST', 'GET'])
def datenschutz_en():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('datenschutz_de',
                                 lang=lang))
    else:
        lang = 'en'

    address_one, address_two, email = helper.get_privacy_legal_notice()

    return render_template('/datenschutz.html',
                            title="PRIVACY NOTICE (ONLY AVAILABLE IN GERMAN)",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index",
                            lang=lang)


@app.route('/de/datenschutz', methods=['POST', 'GET'])
def datenschutz_de():

    if request.method == "POST":
        lang = request.form.get("lang")

        return redirect(url_for('datenschutz_en',
                                 lang=lang))
    else:
        lang = 'de'

    address_one, address_two, email = helper.get_privacy_legal_notice()

    return render_template('/datenschutz.html',
                            title="DATENSCHUTZ",
                            address_one=address_one,
                            address_two=address_two,
                            email=email,
                            id="index",
                            lang=lang)


@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])
