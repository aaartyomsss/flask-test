import psycopg2
import config

def get_db_connection():
    conn = psycopg2.connect(
        host='postgres',
        database=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
    return conn