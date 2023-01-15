from db_utils.init_db import get_db_connection
from db_utils.message import add_new_text_to_table, get_all_messages
from datetime import datetime

def test_if_test_db_can_be_used(app_context):
    with app_context:
        conn = get_db_connection()
        assert conn is not None


def test_amount_of_tables(app_context):
    with app_context:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""SELECT table_name FROM information_schema.tables
                       WHERE table_schema = 'public'""")
        
        tables = cur.fetchall()
        assert len(tables) == 1


def test_insertion_works(app_context):
    with app_context:
        date = datetime.now()
        add_new_text_to_table('sample', date)

        msgs = get_all_messages()

        assert len(msgs) == 1
        msg = msgs[0]
        id, text, date = msg
        assert text == 'sample'

