from utils.webhook import URL, send_data_to_slack_webhook
from datetime import datetime
import pytest

def mocked_request(response_json, status_code, *args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
    
    if response_json and status_code:
        return MockResponse(response_json, status_code)

    return MockResponse(None, 404)

@pytest.fixture
def requests(mocker):
    return mocker.patch('utils.webhook.requests')

def test_webhook_with_text_and_data(mocker):    
    return_value = mocked_request('Mocked response', status_code=200)
    mocker.patch('utils.webhook.post_request', return_value=return_value)


    res = send_data_to_slack_webhook('text', datetime.now())

    assert res == 'ok'


def test_webhook_with_empty_payload(mocker):
    '''
        Yet again, it seems that date is not required
    '''
    mocked_response = {
        'error': 'missing_field_value', 
        'ok': False, 
        'response_metadata': {
            'messages': ["[ERROR] empty required field: 'text'"]
        }
    }
    return_value = mocked_request(mocked_response, status_code=400)
    mocker.patch('utils.webhook.post_request', return_value=return_value)

    res = send_data_to_slack_webhook('', '')

    assert res == mocked_response
