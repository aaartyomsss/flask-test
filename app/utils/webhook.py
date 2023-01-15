import requests
URL = 'https://hooks.slack.com/workflows/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'

def post_request(payload):
    return requests.post(URL, json=payload)

def send_data_to_slack_webhook(text='', date=None):
    payload = {}
    '''
        The addition of the payload is done liek that to
        'force' the error from slack webhook. It expect the
        text field, but it doesn't have the empty string
        validation
    '''
    if text:
        payload['text'] = text
    if date:
        payload['date'] = date.isoformat()

    res = post_request(payload)

    if res.status_code != 200:
        return res.json()
    return 'ok'
