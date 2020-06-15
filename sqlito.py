# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:26:30 2020

@author: Ditto Castform
"""

import sqlite3
from sqlite3 import Error

 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn

def create_table(create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    database = "database/chuzobase.db"
 
    # create a database connection
    conn = create_connection(database)
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        

crear_instas = "CREATE TABLE IF NOT EXISTS instas (user text PRIMARY KEY);"

def agg_insta(user):
    
    database  = "database/chuzobase.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:

        sql = ''' INSERT INTO instas(user)
              VALUES(?) '''
        cur = conn.cursor()
        cur.execute(sql, (user,))
        return cur.lastrowid

def get_instas():
    database = "database/chuzobase.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM instas")
 
        rows = cur.fetchall()
        return rows

def update_insta(x,y):
    database = "database/chuzobase.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:    
        cur = conn.cursor()
        sql = 'UPDATE instas SET user = ? WHERE user = ?'
        cur.execute(sql, (y,x))
        conn.commit()

