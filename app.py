from flask import Flask, jsonify, session, render_template, request, Response, redirect
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('/index.html')

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    return render_template('/portfolio.html')

@app.route('/about', methods=['POST', 'GET'])
def about():

    return render_template('/about.html')
