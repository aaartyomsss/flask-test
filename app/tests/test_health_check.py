
def test_health_check():
    assert True

def test_if_test_client_works(test_client):
    res = test_client.get('/')
    assert res.status_code == 200