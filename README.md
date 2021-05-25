# Portfolio Website for my Data Science Projects
This project showcases my data science projects on a deployed website.

**Latest update:** The color of the navbar was changed.

**05/25/2021:** I linked the latest blog post and project on the index page to the database and removed the hard-coded text from the HTML. The  maximum content width was limited by putting everything into containers.

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [To Do](#todo)
4. [Instructions](#instructions)
    1. [Create Database for Content](#create_database)
    2. [Updating Database Content](#update_database)
5. [File Descriptions](#descriptions)
6. [Licensing, Authors, Acknowledgements](#licensing)


## Installation
The code requires Python versions of 3.* and general libraries available through the Anaconda package. In addition, psycopg2 for the PostgreSQL database, Flask, Werkzeug and gunicorn need to be installed to be able to deploy the website. Please refer to the `requirements.txt` file for more details on dependencies.

## Project Motivation <a name="motivation"></a>
I wanted to have a space to showcase my projects with references to their code, blog posts and deployed apps, where applicable. I also added more details about my learning path towards data science and the skills I acquired.

## To Do <a name="todo"></a>
1. **TODO**: Change layout of Portfolio page
2. **TODO**: Change color scheme
3. **TODO**: Add some JavaScript to make the look nicer

## Instructions <a name="instructions"></a>

### Create Database for Content <a name="create_database"></a>
The database containing the content for the website is a PostgreSQL database on Heroku.

If you want to update the database, you need to connect to the remote database in your local environment. Follow the below steps to connect to a Heroku PostgreSQL database locally:
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
2. Create a PostgreSQL database on [Heroku](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) that is linked to this app.
3. Install PostgreSQL on your computer locally and update your PATH environment variable to add the bin directory of your Postgres installation. (More details [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup))
4. Get the database credentials by running `heroku pg:credentials:url -a <your app name>`. Copy the Connection URL.
5. Type into your shell `$ export DATABASE_URL=postgres://<Connection URL>` if you're using a Mac or Linux and `$ set DATABASE_URL=postgres://<Connection URL>` if you're using Windows. (See the documentation [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup))

Now your local environment has the DATABASE_URL for your remote Heroku PostgreSQL database saved and the code in app.py can access this database from your local computer.

### Update Database Content <a name="update_database"></a>
If you want to update the database content, you need to create Excel files containing the relevant information you want to display on the website.

Running `python database_feeder.py` will read the data from the Excel files into the database.

**Please note**: There is currently no feature in this file that deletes and creates a new database if a new column is added. Adding of rows is handled, but not of columns. Therefore, if you want to add a new column to the Excel file and then database, you need to first reset the PostgreSQL in the app on Heroku and then you need to add the relevant code to the script, before running it.

## File Description <a name="descriptions"></a>
The `templates` folder contains all html pages that will be accessible through the site. The `static` folder is made up of the images displayed on my website, the robots.txt site as well as the css stylesheet. `app.py` is the file which will render the website through the micro web framework Flask. `database_feeder.py` is the script that reads in the data from the Excel files into the database. And the `helper.py` file contains the functions querying the database when a html page is rendered.

## Licensing, Authors, Acknowledgements <a name="licensing"></a>
This code can be used under the [MIT license](https://github.com/julianikulski/portfolio-website/blob/master/LICENSE.md). I created this website completely from scratch, therefore I am the author of the code, including certain references and code snippets from other people which I marked appropriately. Feel free use the code - but remove any of the content relating to me - to create your own portfolio website.
