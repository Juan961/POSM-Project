import sqlite3


conn = sqlite3.connect("./data/db.db")


def get_conn():
    return conn


def get_cursor():
    return conn.cursor()


def commit_db():
    return conn.commit()
