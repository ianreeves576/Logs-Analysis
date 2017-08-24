# Logs-Analysis
## What Does The Program Do?
-This is a program that runs Python Code that runs queries that extracts three specific questions from the database.

In this project I created a reporting tool that prints text from data on the database that answer the following questions:

-What are the most popular three articles of all time?
-Who are the most popular article authors of all time?
-On which days did more than 1% of requests lead to errors?

## What Is Required
-In the Repo is a requirements.txt file that lists the required installations in order to run the program.
-The Python Version that is needed to run the following queries is Python 3.6.

## Installation Instructions
### Installing The Database
1. Install Pycharm 2017.1.5
2. Download the newsdata (1).zip file, located in the Logs-Analysis repo.
3. Unzip the newsdata (1).zip file and find newsdata.sql file located inside.
4. Open newsdata.sql in Pycharm, and there you will be able to create your new database.

### Running The Program
1. First Fork and Clone the Logs-Analysis Repo. 
2. Then, add the files located in the Logs-Analysis Repo into PyCharm
3. Finally, run the python file called 'query_runner.py' by typing in the command "python query_runner.py" in your command line or the terminal located in PyCharm.

## About the files.
In this project, there is a file that coneects to the database (newsdata.sql), one that formats the print statements properly, One that connects the code to the database, and individual files that run queries and print statements that make it easy for the viewer to understand. Finally, a file called 'query_runner.py'was created to import the files containing the queries and print them out one after the other. 
