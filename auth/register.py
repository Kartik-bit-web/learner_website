from flask import Blueprint, render_template, request, redirect, session, url_for, flash

from modules.databaseconnection import mydb
from auth.mailsender import *

register = Blueprint('register', __name__, template_folder='templates', static_folder='static')

from modules.registration import registration

#Here is logic of Registration for Users
@register.get('/')
def register_me():
    return render_template('resigration/registration.html')

@register.post('/')
def resister_post():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pas = request.form.get('password')
    cursor = mydb.cursor()
    cursor.execute('SELECT email FROM register_users')
    x = cursor.fetchall()
    for i in x: 
        if email == i[0]:
            flash('Email already Exist')
            return redirect(url_for('login.login_me'))
        
    code = emailOtpSender(email)
    flash('Code In Your Email have been set successfully')
    session['fname'] = fname
    session['lname'] = lname
    session['email'] = email
    session['pas'] =  pas
    session['email_otp'] = code
    return redirect(url_for('register.emailVerifyForRegister'))

@register.route('/verifyEmailAddress', methods=['POST', 'GET'])
def emailVerifyForRegister():
    flash('Check your Email and enter the six disit code')
    if request.method == 'POST':
        code = request.form.get('code')
        if int(code) == int(session.get('email_otp')):
            #Here is database entry
            commit = registration(session.get('fname'),
                         session.get('lname'),
                         session.get('email'),
                         session.get('pas'))
            commit.Insert_it()

            flash('Congratulations You have been Register Successfully')
            return redirect(url_for('login.login_me'))
    return render_template('resigration/emailverify.html')