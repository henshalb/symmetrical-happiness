from app import create_app

def test_user_login_action_gepo(test_client):
    post_response = test_client.post('/login_action',\
        data=dict(username='henshalb',
    password='0220'), follow_redirects=True)
    get_response = test_client.post('/login_action')
    assert post_response.status_code == 200
    assert get_response.status_code == 400

def test_loginspec_gepo(test_client):
    post_response = test_client.post('/loginspec',\
        data=dict(username='henshalb',
    password='0220'), follow_redirects=True)
    get_response = test_client.post('/loginspec')
    assert post_response.status_code == 400
    assert get_response.status_code == 400

def test_user_logout_gepo(test_client):
    get_response = test_client.get('/logout')
    post_response = test_client.post('/logout')
    # redirect offered
    assert get_response.status_code == 302
    assert post_response.status_code == 405