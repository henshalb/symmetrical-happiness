from flask import render_template,request,\
    jsonify,session,redirect,url_for
from flask.templating import render_template_string
from . import main
from .routes import connection
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'USER_LOGGED_IN' in session:
            return render_template('loginspec.html', next=request.url)
        return f(*args, **kwargs)
    return decorated_function


@main.route('/q/<username>',methods=['GET'])
@login_required
def result(username):
    cursor = connection.cursor()
    sqlko = "select doctor_fullname from doctor where doctor_username = %s"
    datako = (username)
    connection.ping(reconnect=True)
    cursor.execute(sqlko, datako)
    out = cursor.fetchone()
    name = session['USER_DISPLAY_NAME']
    return render_template('result.html',doctor_name=out[0],name=name)
    