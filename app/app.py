from flask import Flask
from db_utils.migrations import run_migrations as _run_migrations
from routes.textarea import textarea

def create_app():
    app = Flask(__name__)
    app.register_blueprint(textarea)

    # FIXME: Could have been done via blueprint as well apparently
    @app.cli.command('migrate')
    def run_migrations():
        _run_migrations()

    return app
    

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')