from flask import (render_template, flash, session,\
    request, redirect, url_for)
from . import main
from passlib.hash import sha256_crypt
from .routes import connection

@main.route("/login")
def user_login():
    return render_template('user_login.html')

@main.route("/register")
def user_register():
    return render_template("user_register.html")


@main.route("/login_action", methods=['POST'])
def user_login_action():
    user_username = request.form['username']
    user_password = request.form['password']

    if request.method == 'POST':
        # with connection:
        cursor = connection.cursor()
        sql = "SELECT user_username FROM user WHERE user_username = %s"
        data = (user_username)
        connection.ping(reconnect=True)
        is_exist = cursor.execute(sql, data)

        if is_exist > 0:
            # with connection:
            cursor = connection.cursor()
            sql = "SELECT user_password FROM user WHERE user_username = %s"
            data = (user_username)
            connection.ping(reconnect=True)
            cursor.execute(sql, data)
            account = cursor.fetchone()
            password_hash = account[0]

            if sha256_crypt.verify(user_password, password_hash):
                # with connection:
                cursor = connection.cursor()
                sql1 = "SELECT user_username,user_fullname FROM user WHERE user_username = %s"
                data1 = (user_username)
                connection.ping(reconnect=True)
                cursor.execute(sql1, data1)
                account1 = cursor.fetchone()

                session['USER_LOGGED_IN'] = 'USER_LOGGED_IN'
                session['USER_DISPLAY_NAME'] = account1[1]
                session['USER_USERNAME'] = account1[0]

                return redirect(url_for('main.landing'))
            else:
                flash("Wrong Password. Try again.")
                return render_template('user_login.html')
        else:
            flash('Unknown credentials.')
            return render_template('user_login.html')




@main.route("/register_action", methods=['POST'])
def user_register_action():

    user_username = request.form['username']
    user_password = request.form['password']
    user_fullname = request.form['fullname']

    if request.method == 'POST' and user_fullname and user_username and user_password:

        # with connection:
        cursor = connection.cursor()
        sql = "SELECT user_username FROM user WHERE user_username = %s"
        data = (user_username)
        connection.ping(reconnect=True)
        cursor.execute(sql, data)
        account = cursor.fetchone()

        if account:

            flash('Username taken, try new one.')
            return render_template('user_register.html')

        else:
            # with connection:
            cursor = connection.cursor()
            user_password_hash = sha256_crypt.encrypt(user_password)
            sql = "INSERT INTO user(user_username, user_fullname, \
                user_password) VALUES(%s,%s,%s)"

            data = (user_username, user_fullname, user_password_hash)
            connection.ping(reconnect=True)
            cursor.execute(sql, data)
            flash('Registration successful, now log in.')
            return render_template('user_login.html')

    else:
        flash('Fill all inputs.')
        return render_template('user_register.html')



@main.route("/loginspec", methods=['GET','POST'])
def loginspec():
    username = request.form['username']
    password = request.form['password']
    next = request.form['URL']

    if request.method == 'POST':
        # with connection:
        cursor = connection.cursor()
        sql = "SELECT user_username FROM user WHERE user_username = %s"
        data = (username)
        connection.ping(reconnect=True)
        yes = cursor.execute(sql, data)

        if yes > 0:
            # with connection:
            cursor = connection.cursor()
            sql = "SELECT user_password FROM user WHERE user_username = %s"
            data = (username)
            connection.ping(reconnect=True)
            cursor.execute(sql, data)
            account = cursor.fetchone()
            xpass = account[0]

            if sha256_crypt.verify(password, xpass):
                # with connection:
                cursor = connection.cursor()
                sql1 = "SELECT user_username,user_fullname FROM user WHERE user_username = %s"
                data1 = (username)
                connection.ping(reconnect=True)
                cursor.execute(sql1, data1)
                account1 = cursor.fetchone()

                session['USER_DISPLAY_NAME'] = account1[1]
                session['USER_LOGGED_IN'] = 'userloggedin'
                session['USER_USERNAME'] = account1[0]

                if next:
                    return redirect(next)

                return redirect(url_for('main.landing'))
            else:
                flash("Wrong Password. Try again.")
                return render_template('login.html')
        else:
            flash('Unknown credentials.')
            return render_template('login.html')
    else:
        flash('Something not right!')
        return render_template('login.html')


@main.route('/logout')
def user_logout():
    session.clear()
    flash('Successfully logged out.')
    return redirect(url_for('main.landing'))
