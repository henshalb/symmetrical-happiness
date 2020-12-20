# must be added to environment variables
# in production and secrets must be
# added to env variables
from pymysql.connections import DEBUG


class Config:
    SECRET_KEY = 'to_be_dynamic_in_production'

# class ConfigTesting(Config):
#     TESTING = True

class DatabaseConfig():
    def __init__(self,host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

db_point_dev = DatabaseConfig('localhost','henshalb','0220','happiness')