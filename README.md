# news
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. This is Log Analysis project by [Udacity](udacity.com) in which you will build out a reporting tool that summarize a large database using SQL.
# Documentation
Please refer to @ psycopg for more info on how the database adapter for the Python programming language was used. 
## create view

Two views were created for question 1 and 2 and used in @ newsdata.py to shorten Sql code
1. create view Q1 as
select articles.title, count(*) as views from articles join log on articles.slug = (regexp_split_to_array(path, E'/article/'))[2] where path != '/' group by (regexp_split_to_array(path, E'/article/'))
[2], articles.title order by views desc limit 3;

2. create view Q2 as 
select authors.name, count(log.path) AS views FROM authors LEFT JOIN articles ON authors.id = articles.author LEFT JOIN log ON log.path LIKE CONCAT('%', articles.slug) GROUP BY authors.name ORDER BY views DESC"
# Installation
The database code to connect to @newsdata.sql is found in @newsdata.py. After forking and cloing the file, open your git command line and connect to the database news using ```psql -d news``` . After that run @ newsdata.py using the following code ```python newdata.py```
# Author
Girum Hagos
# More information
- [psycopg](http://initd.org/psycopg/docs/)
- [psql](https://www.postgresql.org/)