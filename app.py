from flask import Flask, jsonify, session, render_template, request, Response, redirect, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    title_text = "Ich bin passionierte Hobby-Programmiererin und Data Scientist. \
                 "

    return render_template('/index.html',
                            title_text=title_text,
                            title="DATA SCIENCE & SUSTAINABILITY",
                            id="index")

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    projects=[]

    corona = ["The Political and Economic Consequences of COVID-19",
              "Eine Explorative Datenanalyse von Finanz-, Nachrichten-, Umfrage- \
              und Falldaten zum Thema Coronavirus, um politische \
              und ökonomische Auswirkungen einzuschätzen.",
              "Python, EDA, Data Visualization (Matplotlib, Seaborn, Plotly)",
              "covid-19",
              [["Blog Post", "https://towardsdatascience.com/the-political-and-economic-perspective-of-covid-19-c35c046ceffc"],
              ["Code", "https://github.com/julianikulski/covid-19"]]]

    projects.append(corona)

    algorithms = ["Ultimate Guide to AdaBoost, XGBoost, LightGBM",
                  "Eine tiefgehende Analyse und Beschreibung zur Funktionalität \
                  von drei Tree-Based Ensemble Algorithms sowie der Unterscheidung \
                  von Boosting and Bagging.",
                  "Algorithms, Scientific Literacy, Supervised ML Concepts",
                  "ultimate-guide",
                  [["Blog Post", "https://towardsdatascience.com/the-ultimate-guide-to-adaboost-random-forests-and-xgboost-7f9327061c4f"]]]

    projects.append(algorithms)

    time_series = ["Times Series Forecasting Bike Sharing",
                   "Mithilfe von Tree-Based Ensemble Algorithms habe ich tägliche \
                   Bikeshare-Nachfragemengen prognostiziert, unter Berücksichtigung des Look-Ahead-\
                   Bias.",
                   "Python, EDA, Time Series Analysis, Supervised ML, Statistics, \
                   Data Visualization (Matplotlib, Seaborn)",
                   "time-series",
                   [["Blog Post", "https://towardsdatascience.com/go-highly-accurate-or-go-home-61828afb0b13"],
                   ["Code", "https://github.com/julianikulski/bike-sharing"]]]

    projects.append(time_series)

    movie_rev = ["Movie Revenue Prediction",
                 "Mithilfe von AdaBoost, XGBoost und LightGBM und einem Datensatz \
                 von The Movie Database habe ich die Einnahmen von Filmen prognostiziert.",
                 "Python, Supervised ML, Feature Engineering and Selection, \
                 Data Visualization (Matplotlib, Seaborn)",
                 "movie-prediction",
                 [["Blog Post", "https://towardsdatascience.com/predicting-movie-revenue-with-adaboost-xgboost-and-lightgbm-262eadee6daa"],
                 ["Code", "https://github.com/julianikulski/tmdb"]]]

    projects.append(movie_rev)

    recom_eng = ["Recommendation Engines",
                 "Für einen Datensatz von IBM Watson Studios habe ich verschiedene \
                 Recommendation Systems entworfen, um relevante Artikel für User \
                 zu empfehlen.",
                 "Python, Data Wrangling, Recommendation Engines",
                 "recommendation-system",
                 [["Code", "https://github.com/julianikulski/recommendations-with-ibm"]]]

    projects.append(recom_eng)

    disaster = ["Disaster Response Pipeline",
                "Mithilfe von Natural Language Processing und einer ETL-Pipeline \
                habe ich einen Datensatz von Tweets in verschiedene Themenbereiche kategorisiert.",
                "Python, HTML, CSS, Plotly, NLP, ETL & ML Pipelines",
                "disaster-response-pipeline",
                [["Code", "https://github.com/julianikulski/disaster-response-pipeline"]]]

    projects.append(disaster)

    climate_change = ["Climate Change Dashboard",
                      "Ich habe Plotly verwendet, um einen Überblick über Daten zum Klimawandel \
                      herausgegeben von der Weltbank in verschiedenen interaktiven Grafiken darzustellen.",
                      "Python, HTML, CSS, JavaScript, Flask, Data Visualization (Plotly)",
                      "climate-change-dashboard",
                      [["Code", "https://github.com/julianikulski/climate-change-data"]]]

    projects.append(climate_change)

    web_crawler = ["Web Crawler for Job Listings",
                   "Webcrawler, der täglich auf Karriereseiten von \
                   Unternehmen neue Jobs sucht, die Links in einer PostgreSQL Datenbank \
                   speichert und Telegram-Nachrichten an den User versenden.",
                   "Python, PostgreSQL, Webcrawling, App Deployment",
                   "job-scraper",
                   [["Blog Post", "https://medium.com/@julia.nikulski/building-a-job-listings-web-scraper-that-sends-out-telegram-notifications-830763890a92"]]]

    projects.append(web_crawler)

    airbnb = ["Analysis of the Airbnb Market in Boston",
              "Eine explorative Datenanalyse von Airbnb-Listings und -Bookings in \
              Boston, USA, mit der Visualisierung der Ergebnisse.",
              "Python, Statistical Hypothesis Testing, Data Visualization (Matplotlib, \
              Seaborn)",
              "airbnb",
              [["Blog Post", "https://medium.com/@julia.nikulski/here-is-what-you-need-to-know-about-staying-in-boston-with-airbnb-57e81f5296ae"],
              ["Code", "https://github.com/julianikulski/boston-airbnb-data"]]]

    projects.append(airbnb)

    cust_seg = ["Identifying Customer Segments",
                "Mithilfe von PCA und K-Means Clustering habe ich potentielle Kundensegmente \
                in der deutschen Bevölkerung für einen Versandhandel identifiziert.",
                "Python, Unsupervised ML, Feature Engineering and Selection, PCA, K-Means Clustering",
                "customer-segments",
                [["Code", "https://github.com/julianikulski/identifying-customer-segments"]]]

    projects.append(cust_seg)

    image_class = ["Deep Learning Image Classifier",
                   "Ich habe ein Bild-Klassifizierungs-Modell mithilfe von PyTorch \
                   entwickelt, welches Bilder von Blumen in 102 verschiedene Kategorien \
                   von Blumen einordnen kann.",
                   "Python, Deep Learning, PyTorch",
                   "image-classifier",
                   [["Code", "https://github.com/julianikulski/image-classifier-projects"]]]

    projects.append(image_class)

    donors = ["Finding Donors for Charity",
              "Performance-Vergleich verschiedener Supervised \
              ML Algorithmen (Naive Bayes, Decision Trees, Random Forests, \
              AdaBoost), um potentielle Spender zu identifizieren.",
              "Python, Supervised ML, Feature Engineering and Selection",
              "identifying-donors",
              [["Code", "https://github.com/julianikulski/finding-donors"]]]

    projects.append(donors)

    if len(projects) % 2 == 0:
        pass
    else:
        projects.append(['placeholder'])

    iterator = iter(projects)
    zipped = zip(iterator, iterator)

    title_text = "Ich habe verschiedenste Projekte implementiert. Mein neuestes ist diese \
                 Website, die ich mit Flask erstellt habe. Weiter unten stelle ich meine anderen \
                 Projekte vor und verlinke zum Code, meinen Blog Posts und den gehosteten Projekten"

    return render_template('/portfolio.html',
                            title_text=title_text,
                            title="PROJEKTPORTFOLIO",
                            id="portfolio",
                            projects=zipped)

@app.route('/about', methods=['POST', 'GET'])
def about():

    title_text = "Seit 2018 "

    return render_template('/about.html',
                            title_text=title_text,
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
