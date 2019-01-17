#!/usr/bin/env python2.7

import psycopg2


DATABASE_NAME = "news"


def runquery(query):
    """
        Takes a query as parameter, runs against the database
        and returns the results
    """
    db = psycopg2.connect(database=DATABASE_NAME)
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results


def main():
    """Main function of the program - to be run first"""
    print ""
    question_one()
    question_two()
    question_three()


def question_one():
    """First question - holds query and controls output"""
    query = """
        SELECT DISTINCT
            articles.title,
            COUNT(log.id) as "number"
        FROM
            articles,
            log
        WHERE
            log.path = '/article/' || articles.slug
        GROUP BY
            articles.title
        ORDER BY
            number
        DESC LIMIT 3;
        """
    print "1. What are the most popular three articles of all time?"
    rows = runquery(query)
    for row in rows:
        print str(row[0]) + " - " + str(row[1]) + " views"
    print ""


def question_two():
    """Second question - holds query and controls output"""
    query = """
        SELECT DISTINCT
            authors.name,
            COUNT(log.id) as "number"
        FROM
            authors,
            articles,
            log
        WHERE
            log.path = '/article/' || articles.slug
        AND
            authors.id = articles.author
        GROUP BY
            authors.name
        ORDER BY
            number DESC;
        """
    print "2. Who are the most popular article authors of all time?"
    rows = runquery(query)
    for row in rows:
        print str(row[0]) + " - " + str(row[1]) + " views"
    print ""


def question_three():
    """Third question - holds query and controls output
        A note about the query: originally the date format was:
        'Month DD, YYYY'
        Changing to 'FMMonth' removes extra spaces.
        More at this link:
        https://www.postgresql.org/docs/10/functions-formatting
        .html#FUNCTIONS-FORMATTING-DATETIMEMOD-TABLE
    """
    query = """
        SELECT
            TO_CHAR(errors.date,'FMMonth DD, YYYY') AS date,
            TO_CHAR(((errors.count::decimal
                    /requests.count::decimal)*100)
                    ,'9.99') AS percentage
        FROM
            (SELECT date(time),count(*)
                FROM log
                GROUP BY date(time)) AS requests,
            (SELECT date(time),count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY date(time)) AS errors
        WHERE
            requests.date = errors.date
        AND
            ((errors.count::decimal
                    /requests.count::decimal)*100) > 1;
        """
    print "3. On which days did more than 1% of requests lead to errors?"
    rows = runquery(query)
    for row in rows:
        print str(row[0]) + " - " + str(row[1]) + "% errors"
    print ""


main()
