import psycopg2
import config
from flask import current_app


def get_db_connection():
    is_test = current_app.config.get('TESTING', False)

    kwargs = {
        'host': 'postgres'
    }

    if not is_test:
        kwargs['database']= config.DB_NAME
        kwargs['user'] = config.DB_USER
        kwargs['password'] = config.DB_PASSWORD
    else:
        kwargs['database']= config.TEST_DB_NAME
        kwargs['user'] = config.TEST_DB_USER
        kwargs['password'] = config.TEST_DB_PASSWORD

    conn = psycopg2.connect(
        **kwargs
    )
    return conn