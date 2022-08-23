import sqlite3

conn = sqlite3.connect("lottodb.sqlite")

cur = conn.cursor()

sql_query = """ CREATE TABLE lotto (
    id integer PRIMARY KEY UNIQUE,
    nlotto text NOT NULL,
    nplus text NULL,
    superid integer NULL,
    date text NOT NULL,
    time text NULL
    )"""
cur.execute(sql_query)