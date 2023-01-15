from db_utils.message import create_message_table, drop_table_message

def run_migrations():
    create_message_table()
    # Here theoretic other migrations will go

def run_teardown():
    # Needed for testing!!!
    # super risky in production
    drop_table_message()
