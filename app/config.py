# must be added to environment variables
# in production and secrets must be
# added to env variables
class Config:
    SECRET_KEY = 'to_be_dynamic_in_production'
    TESTING = True
class ConfigDbDev():
    host = 'localhost'
    user= 'henshalb'
    password='0220'
    db='happiness'
class ConfigDbTest():
    host = 'localhost'
    user= 'henshalb'
    password='0220'
    db='happiness'
db_point_dev = ConfigDbDev()
db_point_test = ConfigDbTest()