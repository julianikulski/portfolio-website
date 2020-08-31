from flask import request
import psycopg2
import os


def check_language(sql_query_en, sql_query_de, lang):
    '''
    Function to check language and choose correct table in database
    Args: sql_query_en = str; contains the sql_query for English
          sql_query_de = str; contains the sql_query for German
          lang = str; language
    Returns: df_row = contains results from sql query
    '''

    # connect to database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select everything from the titles database
    if lang == 'de':
        cur.execute(sql_query_de)
        db_row = cur.fetchall()
        # close database connection
        conn.close()
    elif lang == 'en':
        cur.execute(sql_query_en)
        db_row = cur.fetchall()
        # close database connection
        conn.close()
    else:
        cur.execute(sql_query_de)
        db_row = cur.fetchall()
        # close database connection
        conn.close()

    return db_row


def get_title_content(page, lang):
    '''
    Function to get the relevant content for the html page
    Args: page = str; name of the html page
          lang = str; specifies language selected by user
    Returns: title_text = str; content for the html page
    '''

    db_row = check_language("SELECT content FROM titles_en",
                            "SELECT content FROM titles",
                            lang)

    # assign content to variable
    if page == 'index':
        title_text = db_row[0][0]
    elif page == 'portfolio':
        title_text = db_row[1][0]
    elif page == 'about':
        title_text = db_row[2][0]

    return title_text

def get_portfolio_content(lang):
    '''
    Function to get the portfolio projects from the database
    Args: lang = str; specifies language selected by user
    Returns: zipped
    '''

    db_row = check_language("SELECT * FROM portfolio_en",
                            "SELECT * FROM portfolio",
                            lang)

    # instantiate a list to save all projects in
    project_list = []
    # iterate through all the projects in the database
    for project in db_row:
        one_project = []
        # add the title, description, skills and image name
        one_project.extend(project[1:5])
        # instantiate list for links
        links = []
        if project[6] != 'NaN':
            links.append(["Blog Post", project[6]])
        if project[5] != 'NaN':
            links.append(["Code", project[5]])
        one_project.append(links)

        # assign single project to entire project_list
        project_list.append(one_project)

    # create list of lists that contains pairs of projects
    if len(project_list) % 2 == 0:
        pass
    else:
        project_list.append(['placeholder'])
    iterator = iter(project_list)
    zipped = zip(iterator, iterator)

    return zipped

def get_skill_content(lang):
    '''
    Function to get the skills from the database
    Args: lang = str; specifies language selected by user
    Returns: skill_list
    '''

    db_row = check_language("SELECT * FROM skills_en",
                            "SELECT * FROM skills",
                            lang)

    # instantiate a dict to save all projects in
    skill_dict = {}

    # iterate through all the skills in the database
    for skill in db_row:
        if skill[1] in skill_dict.keys():
            skill_dict[skill[1]].append(list(skill[2:5]))
        else:
            skill_dict[skill[1]] = [list(skill[2:5])]

    return skill_dict
