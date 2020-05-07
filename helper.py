import psycopg2
import os


def get_title_content(page):
    '''
    Function to get the relevant content for the html page
    Args: page = str; name of the html page
    Returns: title_text = str; content for the html page
    '''
    # connect to database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select everything from the titles database
    cur.execute("SELECT content FROM titles WHERE page=%s",
                 [page])
    db_row = cur.fetchall()
    # close database connection
    conn.close()

    # assign content to variable
    title_text = db_row[0][0]

    return title_text
