from flask import render_template,request,jsonify
from . import main
import pymysql

connection = pymysql.connect(host='localhost',
                             user='henshalb',
                             password='0220',
                             db='newdb',
                             charset='utf8mb4',
                             autocommit=True)

@main.route('/',methods=['GET','POST'])
def landing():
    return render_template('landing.html')

@main.route('/search_doctor_ajax',methods=['POST'])
def user_search_doctor_from_home():
    data = request.form.get('text')
    cursor = connection.cursor()
    percent = data+'%'
    search_query = "select doctor_fullname,doctor_username from doctor where \
        doctor_fullname LIKE %s ORDER BY doctor_fullname"
    data_query = (percent)
    connection.ping(reconnect=True)
    cursor.execute(search_query, data_query)
    result = cursor.fetchall()
    return jsonify(result)