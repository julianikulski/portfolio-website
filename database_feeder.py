import pandas as pd
import numpy as np
import psycopg2
import os

# read in all necessary Excel files
content_df = pd.read_excel("content_db.xlsx")
titles_df = pd.read_excel("titles_db.xlsx")

# connect and create tables if they don't exist yet
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS content \
            (id SERIAL, title text NOT NULL, description text, skills text, \
             image text, code text, blog_post text, project text, date date, tag text)")

cur.execute("CREATE TABLE IF NOT EXISTS titles \
            (id SERIAL, page text, content text)")

# select everything from the titles database
cur.execute("SELECT * FROM titles")
db_row = cur.fetchall()
db_row_page = [x[1] for x in db_row]

# read the data into the titles database
# iterate through the dataframe generated from the Excel file
for titles_row in titles_df.itertuples():
    # check whether the page is already on the website
    if titles_row.page in db_row_page:
        # get the row number/index of the particular page value
        item_index = db_row_page.index(titles_row.page)
        # check whether the content for the page is different from the content
        # in the Excel file
        if titles_row.content == db_row[item_index]:
            pass
        else:
            # update content
            cur.execute("UPDATE titles SET content = %s WHERE page = %s",
                        [titles_row.content, titles_row.page])
            conn.commit()
    else:
        # if the page is not yet on the website, then add a new database entry
        cur.execute("INSERT INTO titles (page, content) VALUES (%s, %s)",
                    [titles_row.page, titles_row.content])
        conn.commit()

conn.close()

# select everything from the titles database
cur.execute("SELECT * FROM titles")
db_row = cur.fetchall()
db_row_page = [x[1] for x in db_row]


cur.execute("SELECT * FROM titles")
row = cur.fetchall()
print(row)
