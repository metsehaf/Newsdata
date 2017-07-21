"""Database code to connect to newsdata.sql."""

import psycopg2

DBNAME = "news"

def Question_1():
    #connect to database news
    db = psycopg2.connect("dbname=news")

    c = db.cursor()

#get the top 3 articles based on the amount of views

    query = "select * from Q1;"
    c.execute(query)

#fetch the results
    rows = c.fetchall()

#Loop through each title, count pairing and print out data for top 3. Reference site https://pyformat.info
    for row in rows:#[:3]:
        print("\nArticle: {:^10} \nViews: {:^10}" .format(row[0], row[1]))
    #print("The Top Three Articles are: ")
        #print("%s " % (row[0]))

#close database
    db.close()

def Question_2():
    #connect to database news
    db = psycopg2.connect("dbname=news")

    c = db.cursor()

#get the top 3 articles based on the amount of views

    query = "select * from Q2;"
    c.execute(query)

#fetch the results
    rows = c.fetchall()

#Loop through each title, count pairing and print out data for top 3. Reference site https://pyformat.info
    for row in rows:
        #print(row[0])
    #print("The Top Three Articles are: ")
        print("\nAuthor: {:^10} \nViews: {:^10}" .format(row[0], row[1]))
#close database
    db.close()

def get_error_percentage():
    #connect to database news
    db = psycopg2.connect("dbname=news")

    c = db.cursor()

#get the top 3 articles based on the amount of views

    query = " select date(time) AS date from log group by date;"
    c.execute(query)

#fetch the results
    rows = c.fetchall()

#Loop through each title, count pairing and print out data for top 3. Reference site https://pyformat.info
    for row in rows:
        print("%s " % (row[0]))
#runs the function to start the queries
if __name__ == '__main__':
    Question_1()
    Question_2()
    get_error_percentage()
