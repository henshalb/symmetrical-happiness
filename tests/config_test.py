# where fixtures are defined

import pytest
import  pymysql
from app.config import db_point_test
from app import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(debug=True)
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client 

@pytest.fixture(scope='module')
def db_connection_test(test_client):
    connection = pymysql.\
    connect(host=db_point_test.host,\
    user=db_point_test.user,\
    password=db_point_test.password,\
    db=db_point_test.db,\
    charset='utf8mb4',\
    autocommit=True)
    return connection



