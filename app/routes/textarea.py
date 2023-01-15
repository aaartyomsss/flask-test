from flask import Blueprint, render_template, request
from db_utils.message import add_new_text_to_table
from datetime import datetime
from utils.webhook import send_data_to_slack_webhook

textarea = Blueprint('textarea', __name__,
                     template_folder='templates')

@textarea.route('/', methods=['GET', 'POST'])
def submit_text():
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            date = datetime.now()
            add_new_text_to_table(text=text, date=date)
            send_data_to_slack_webhook(text=text, date=date)
    return render_template('index.html')