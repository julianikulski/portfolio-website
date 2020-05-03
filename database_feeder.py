import pandas as pd
import psycopg2
import os


content_df = pd.read_excel("own-website-database.xlsx")
for row in content_df.itertuples():
    print(row.title)


DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS content \
            (id SERIAL, title text NOT NULL, description text, skills text, \
             image text, code text, blog_post text, project text, tag text)")
# Query database for username
cur.execute("SELECT * FROM content")
row = cur.fetchall()
