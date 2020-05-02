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

    projects=[]

    corona = ["Political and Economic Consequences of COVID-19",
              "Ich habe eine Explorative Datenanalyse von Finanz-, Nachrichten-, Umfrage- \
              und Falldaten zum Thema Coronavirus durchgeführt, um einen Eindruck der politischen \
              und ökonomischen Auswirkungen zu bekommen",
              "Python, EDA, Data Visualization (Matplotlib, Seaborn, Plotly)",
              "covid-19"]

    projects.append(corona)

    algorithms = ["Ultimate Guide to AdaBoost, XGBoost, LightGBM",
                  "Eine tiefgehende Analyse und Beschreibung zur Funktionalität \
                  von drei Tree-Based Ensemble Algorithms sowie der Unterscheidung \
                  von Boosting and Bagging",
                  "Algorithms, Scientific Literacy, Supervised ML Concepts",
                  "ultimate-guide"]

    projects.append(algorithms)

    time_series = ["Times Series Forecasting Bike Sharing",
                   "Mit Daten von Capital Bikeshare habe ich tägliche Bikeshare-\
                   Nachfragemengen prognostiziert, unter Berücksichtigung des Look-Ahead-\
                   Bias und mithilfe von Tree-Based Ensemble Algorithms",
                   "Python, EDA, Time Series Analysis, Supervised ML, Statistics",
                   "time-series"]

    projects.append(time_series)

    movie_rev = ["Movie Revenue Prediction",
                 "Mithilfe von AdaBoost, XGBoost und LightGBM und einem Datensatz \
                 von The Movie Database habe ich die Einnahmen von Filmen prognostiziert.",
                 "Python, Supervised ML, Feature Engineering, \
                 Data Visualization (Matplotlib, Seaborn",
                 "movie-prediction"]

    projects.append(movie_rev)

    recom_eng = ["Recommendation Engines",
                 "Für einen Datensatz von IBM Watson Studios habe ich verschiedene \
                 Recommendation Systems entworfen, um relevante Artikel für User \
                 zu empfehlen",
                 "Python, Data Wrangling, Recommendation Engines",
                 "recommendation-system"]

    projects.append(recom_eng)

    disaster = ["Disaster Response Pipeline",
                "Mithilfe von Natural Language Processing und einer ETL-Pipeline \
                habe ich einen Datensatz von Tweets in verschiedene Themenbereiche kategorisiert.",
                "Python, HTML, CSS, Plotly, NLP, ETL & ML Pipelines",
                "disaster-response-pipeline"]

    projects.append(disaster)

    #climate_change()

    #projects.append(climate_change)

    cust_seg = ["Identifying Customer Segments",
                "In diesem Unsupervised Machine Learning Projekt habe ich PCA \
                und K-Means Clustering angewendet, um potentielle Kundensegmente \
                in der deutschen Bevölkerung für einen Versandhandel zu identifizieren.",
                "Python, Unsupervised ML, Feature Engineering, PCA, K-Means Clustering \
                Data Visualization (Matplotlib, Seaborn",
                "customer-segments"]

    projects.append(cust_seg)


    if len(projects) % 2 == 0:
        pass
    else:
        projects.append(['placeholder'])

    iterator = iter(projects)
    zipped = zip(iterator, iterator)

    return render_template('/portfolio.html',
                            title="PROJEKTPORTFOLIO",
                            id="portfolio",
                            projects=zipped)

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
