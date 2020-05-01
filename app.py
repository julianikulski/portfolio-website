from flask import Flask, jsonify, session, render_template, request, Response, redirect, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('/index.html',
                            title="DATA SCIENCE & SUSTAINABILITY",
                            id="index")

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    return render_template('/portfolio.html',
                            title="PROJEKTPORTFOLIO",
                            id="portfolio")

@app.route('/about', methods=['POST', 'GET'])
def about():

    return render_template('/about.html',
                            title="ÜBER MICH",
                            id="about")

@app.route('/impressum', methods=['POST', 'GET'])
def impressum():

    return render_template('/impressum.html',
                            title="IMPRESSUM",
                            id="index")

@app.route('/datenschutz', methods=['POST', 'GET'])
def datenschutz():

    return render_template('/datenschutz.html',
                            title="DATENSCHUTZ",
                            id="index")


@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])
