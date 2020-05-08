# Portfolio Website for My Data Science Projects

This project was created among a group of friends during the corona pandemic to allow to play cards against humanity online without meeting in person.

## Table of Contents
1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Instructions](#instructions)
    1. [Create Database for Content](#create_database)
    2. [](#)
4. [File Descriptions](#descriptions)
5. [Licensing, Authors, Acknowledgements](#licensing)


## Installation
The code requires Python versions of 3.* and general libraries available through the Anaconda package. In addition, XXXX

## Project Motivation <a name="motivation"></a>


## Instructions <a name="instructions"></a>

### Database for Content <a name="create_database"></a>

The database containing the content for the website is a PostgreSQL database on Heroku.
If you want to update the database, you need to connect to the remote database in your local environment. Follow the below steps to connect to a Heroku PostgreSQL database locally:
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
2. Create a PostgreSQL database on [Heroku](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) that is linked to this app.
3. Install PostgreSQL on your computer locally and update your PATH environment variable to add the bin directory of your Postgres installation. (More details [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup))
4. Get the database credentials by running `heroku pg:credentials:url -a <your app name>`. Copy the Connection URL.
5. Type into your shell `$ export DATABASE_URL=postgres://<Connection URL>` if you're using a Mac or Linux and `$ set DATABASE_URL=postgres://<Connection URL>` if you're using Windows. (See the documentation [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup))

Now your local environment has the DATABASE_URL for your remote Heroku PostgreSQL database saved and the code in app.py can access this database from your local computer.

###


## Licensing, Authors, Acknowledgements <a name="licensing"></a>
I created this website completely from scratch, therefore I am the author of the code, including certain references and code snippets from other people which I marked appropriately. Feel free use the code to create your own portfolio website.
