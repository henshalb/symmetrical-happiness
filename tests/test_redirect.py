from app import create_app

#  to be a fixure
def test_result():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as testing_client:
        # setting context before request
        with testing_client.session_transaction() as sess:
            sess['USER_LOGGED_IN'] = 'USER_LOGGED_IN'
            sess['USER_DISPLAY_NAME'] = 'Henshal B'
            sess['USER_USERNAME'] = 'henshalb'
        get_response = testing_client.get('/q/amal')
        post_response =testing_client.post('/q/amal')
        assert get_response.status_code == 200
        assert b'Amal KV' in get_response.data
        assert post_response.status_code == 405
        assert b'html' not in post_response.data 