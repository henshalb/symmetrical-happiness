from app import create_app

def test_landing_gepo(test_client):
    get_response = test_client.get('/')
    post_response = test_client.post('/')
    assert get_response.status_code == 200
    assert b'html' in get_response.data
    assert post_response.status_code == 405
    assert b'html' not in post_response.data 


def test_user_search_doctor_from_home_gepo(test_client):
    get_response = test_client.get('/search_doctor_ajax')
    post_response = test_client.post('/search_doctor_ajax',\
        data=dict(text = 'am'), follow_redirects=False)
    assert post_response.status_code == 200
    json_response = post_response.get_json()
    assert 'Amal KV' in json_response[0]
    assert get_response.status_code == 405
