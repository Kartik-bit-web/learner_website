from flask import render_template, request, redirect, url_for, Blueprint, session, flash

from werkzeug.security import check_password_hash
from auth.mailsender import *

from modules.databaseconnection import mydb

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')    

#Here is logic of Login for Users, For those who have already account
@login.get('/')
def login_me():
    return render_template('resigration/login.html')

@login.post('/')
def post_login():
    email = request.form.get('email')
    pas = request.form.get('pass')
    # Here is database Logic 
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register_users')
    x = cursor.fetchall()
    for i in x:
        if (email == i[4] ) and (check_password_hash(i[5], pas) ):
            session['uuid'] = i[1]
            flash('You have been LogIn Successfully')
            return redirect(url_for('home'))
        elif (email==i[4]) and (check_password_hash(i[5], pas) == False ):
            flash('Wrong Password try again:- ')
            return redirect(url_for('login.login_me'))
        
        flash("You Don' have Account in website Please Register Youself:- ")
        return redirect(url_for('register.register_me'))
    

@login.route('/Verification_Email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        email = request.form.get('email')
        val = emailOtpSender(email)
        session['otp'] = val
        return redirect(url_for('public.codeVerificationForForgetPassword'))
    return render_template('email.html')


@login.route('/Verification_code', methods=['POST', 'GET'])
def codeVerificationForForgetPassword():
    if request.method == 'POST':
        code = request.form.get('code')
        if int(code) == int(session.get('otp')):
            print('Successful Verify')
            session.pop('otp')
            return redirect('/resetPassword')
        return "code isn't match"
    return render_template('forgetPassCode.html')



@login.route('/Reset_Password', methods=['GET', 'POST'])
def resetPass():
    if request.method == 'POST':
        
        pass1 = request.form.get('password')
        pass2 = request.form.get('password2')
        if pass1 == pass2:
            return redirect('/login')
    return render_template('resetPassword.html')

@login.route("/logout")
def logout():
    flash('Logout Successfully See You Again:- ')
    session.pop('uuid', None)
    return redirect('/')
