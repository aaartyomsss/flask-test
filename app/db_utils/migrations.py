from db_utils.message import create_message_table

def run_migrations():
    create_message_table()
    # Here theoretic other migrations will go