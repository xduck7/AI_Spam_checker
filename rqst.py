import psycopg2
import names
import datetime
import random

def gen_id():
    id = ''
    alf = '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'
    for x in range(16):
        id = id + random.choice(list(alf))
    return id

def first_start():
    conn = psycopg2.connect(dbname='postgres',
                            user='postgres', 
                            password='postgres', 
                            host='localhost',
                            port='5432')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS forspam ("+
    "ID VARCHAR, " +
    "DATE_TIME VARCHAR, " +
    "AUTHOR VARCHAR, " +
    "CONTENT VARCHAR, " +
    "CLASS VARCHAR )")
    conn.commit()

    cursor.close()
    conn.close()

def add_report(msg, pred):

    id = gen_id()
    author = names.get_first_name()
    date_time = datetime.datetime.now()

    conn = psycopg2.connect(dbname='postgres',
                            user='postgres', 
                            password='postgres', 
                            host='localhost',
                            port='5432')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO forspam (id, date_time, author, content, class) values "+
                    f"('{id}','{date_time}','{author}','{msg}','{pred}')")
    conn.commit()

    cursor.close()
    conn.close()
