import pytest
from .app import create_app
from db_utils.migrations import run_migrations, run_teardown

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        'TESTING': True
    })

    with app.app_context():
        run_migrations()

    yield app

    with app.app_context():
        run_teardown()

@pytest.fixture
def app_context(app):
    return app.app_context()    

@pytest.fixture
def test_client(app):
    return app.test_client()