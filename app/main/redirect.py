from flask import render_template,request,jsonify,session
from . import main
from .routes import connection

@main.route('/q/<username>',methods=['GET'])
def result(username):
    if ('USER_LOGGED_IN' in session):
        cursor = connection.cursor()
        sqlko = "select doctor_fullname from doctor where doctor_username = %s"
        datako = (username)
        connection.ping(reconnect=True)
        cursor.execute(sqlko, datako)
        out = cursor.fetchone()
        name = session['USER_DISPLAY_NAME']
        return render_template('result.html',doctor_name=out[0],name=name)
    else:
        return render_template('loginspec.html')
    