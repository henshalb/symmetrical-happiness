# where fixtures are defined

import pytest
from app import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client



