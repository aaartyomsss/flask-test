from db_utils.message import get_all_messages

def test_text_is_stored(test_client, app_context):
    res = test_client.post('/', data={
        'text': 'text'
    })
    assert res.status_code == 200

    with app_context:
        msgs = get_all_messages()
        assert len(msgs) == 1


def test_empty_message_not_added(test_client, app_context):
    res = test_client.post('/', data={
        'text': ''
    })
    assert res.status_code == 200

    with app_context:
        msgs = get_all_messages()
        assert len(msgs) == 0