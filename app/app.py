from flask import Flask, render_template, request
from db_utils.migrations import run_migrations as _run_migrations
from db_utils.message import add_new_text_to_table
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def template():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            date = datetime.now()
            add_new_text_to_table(text=text, date=date)
    return render_template('index.html')

@app.cli.command('migrate')
def run_migrations():
    _run_migrations()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
