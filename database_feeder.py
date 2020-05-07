import pandas as pd
import numpy as np
import psycopg2
import os

# read in all necessary Excel files
portfolio_df = pd.read_excel("database/portfolio_db.xlsx")
titles_df = pd.read_excel("database/titles_db.xlsx")

# connect and create tables if they don't exist yet
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS portfolio \
            (id SERIAL, title text NOT NULL, description text, skills text, \
             image text, code text, blog_post text, project text, date date, tag text)")

cur.execute("CREATE TABLE IF NOT EXISTS titles \
            (id SERIAL, page text, content text)")

# select everything from the titles database
cur.execute("TRUNCATE titles RESTART IDENTITY")

# read the data into the titles database
# iterate through the dataframe generated from the Excel file
for titles_row in titles_df.itertuples():
    cur.execute("INSERT INTO titles (page, content) VALUES (%s, %s)",
                [titles_row.page, titles_row.content])
    conn.commit()

# select everything from the portfolio database
cur.execute("TRUNCATE portfolio RESTART IDENTITY")

# read the data into the portfolio database
# iterate through the dataframe generated from the Excel file
for portfolio_row in portfolio_df.itertuples():
    cur.execute("INSERT INTO portfolio (title, description, skills, image, code, blog_post, tag) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)",
                [portfolio_row.title, portfolio_row.description,
                 portfolio_row.skills, portfolio_row.image, portfolio_row.code,
                 portfolio_row.blog_post, portfolio_row.tag])
    conn.commit()
