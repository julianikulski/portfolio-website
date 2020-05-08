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

def get_portfolio_content():
    '''
    Function to get the portfolio projects from the database
    Args: None
    Returns: project_list
    '''
    # connect to database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select everything from the portfolio database
    cur.execute("SELECT * FROM portfolio")
    db_row = cur.fetchall()
    # close database connection
    conn.close()

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

    return project_list

def get_skill_content():
    '''
    Function to get the skills from the database
    Args: None
    Returns: skill_list
    '''
    # connect to database
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    # select everything from the skills database
    cur.execute("SELECT * FROM skills")
    db_row = cur.fetchall()
    # close database connection
    conn.close()

    # instantiate a dict to save all projects in
    skill_dict = {}

    # iterate through all the skills in the database
    for skill in db_row:
        if skill[1] in skill_dict.keys():
            skill_dict[skill[1]].append(list(skill[2:4]))
        else:
            skill_dict[skill[1]] = [list(skill[2:4])]

    return skill_dict
