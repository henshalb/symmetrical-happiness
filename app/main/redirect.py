from flask import render_template,request,jsonify
from . import main
from .routes import connection

@main.route('/q/<username>',methods=['GET'])
def result(username):
    cursor = connection.cursor()
    sqlko = "select doctor_fullname from doctor where doctor_username = %s"
    datako = (username)
    connection.ping(reconnect=True)
    cursor.execute(sqlko, datako)
    out = cursor.fetchone()
    return render_template('result.html',doctor_name=out[0])