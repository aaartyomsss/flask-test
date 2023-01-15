from db_utils.init_db import get_db_connection
from psycopg2.errors import DuplicateTable, DatabaseError

def create_message_table():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute('CREATE TABLE message(id serial PRIMARY KEY,'
                                        'text varchar (500) NOT NULL,'
                                        'date date DEFAULT CURRENT_TIMESTAMP);'
                                        )
        conn.commit() 
    except DuplicateTable:
        pass
    cur.close()
    conn.close()


def add_new_text_to_table(text, date):
    sql = """INSERT INTO message(text, date)
             VALUES(%s, %s);"""

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql, (text, date))
        conn.commit()
        cur.close()
    except (Exception, DatabaseError) as error:
        print("-------------------------")
        print(error)
        print("-------------------------")
    finally:
        if conn is not None:
            conn.close()

def get_all_messages():
    sql = "SELECT * FROM message;"
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(sql)
        messages = cur.fetchall()
        conn.commit()
        cur.close()
        return messages
    except (Exception, DatabaseError) as error:
        print("-------------------------")
        print(error)
        print("-------------------------")
    finally:
        if conn is not None:
            conn.close()


def drop_table_message():
    sql = 'DROP TABLE IF EXISTS message;'
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()