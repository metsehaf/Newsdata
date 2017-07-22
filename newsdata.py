#! /usr/bin/env python3
"""Database code to connect to newsdata.sql."""

import psycopg2

DBNAME = "news"

# create a function that establishes the database connection


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def Question_1():
    # connect to database news
    db, cursor = connect()

# get the top 3 articles based on the amount of views

    query = "select * from Q1;"
    cursor.execute(query)

# fetch the results
    rows = cursor.fetchall()

# Loop through each title, count pairing and print out data for top 3.
    for row in rows:
        print("\nArticle: {:^10} \nViews: {:^10}" .format(row[0], row[1]))
# print("The Top Three Articles are: ")
# print("%s " % (row[0]))

# close database
    db.close()


def Question_2():
    # connect to database news
    db, cursor = connect()

# get the top 3 articles based on the amount of views

    query = "select * from Q2;"
    cursor.execute(query)

# fetch the results
    rows = cursor.fetchall()

# Loop through each title, count pairing and print out data for top 3
    for row in rows:
        # print("The Top Three Articles are: ")
        print("\nAuthor: {:^10} \nViews: {:^10}" .format(row[0], row[1]))
# close database
    db.close()


def get_error_percentage():

    # connect to database news
    db, cursor = connect()

# get the top 3 articles based on the amount of views

    query = '''SELECT time::date AS date, (SELECT count(status)::float FROM log)
     AS total , (Select count(status)::float FROM log WHERE status LIKE
     '%404 %') AS error FROM log GROUP BY date ORDER BY date, total, error'''
    cursor.execute(query)

# fetch the results
    rows = cursor.fetchall()

# Loop through each title, count pairing and print out data for top 3
    for row in rows:
        total = (row[2]/row[1]) * 100
        print(row[0], total)
# Runs the function to start the queries
if __name__ == '__main__':
    Question_1()
    Question_2()
    get_error_percentage()
