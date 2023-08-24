from flask import render_template, request, redirect, url_for, Blueprint, session, flash

# Importing sub categories folder and file 
from public_panel.sub_cat.sub_categories import sub_cate

from public_panel.mailsender import *

from modules.databaseconnection import mydb
from modules.registration import registration

from werkzeug.security import check_password_hash

public = Blueprint('public', __name__, template_folder='templates', static_folder='static')

#Here is website's HOME page, Landing page of website
@public.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

#Here is Categories option and its sub category, sub category has different location for more productive
public.register_blueprint(sub_cate, url_prefix='/classes')
@public.route('/classes', methods=['GET', 'POST'])
def category():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM categories')
    x = cursor.fetchall()
    print(x)
    return render_template('category.html', x=x)

#Here is Jst like blog page where user can ask it's problems and shre their Idea's, and keep updating to user for this website
@public.route('/pages', methods=['GET', 'POST'])
def page():
    return render_template('pages.html')

#Here is About section for user to content for a problem or can content directly to support team 
@public.route('/about_us', methods=['GET', 'POST'])
def about():
    return render_template('about_us.html')


#Here is logic of Registration for Users
@public.get('/registration')
def register_me():
    return render_template('resigration/registration.html')

@public.post('/registration')
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
            return redirect(url_for('public.login_me'))
        
    code = emailOtpSender(email)
    flash('Code In Your Email have been set successfully')
    session['fname'] = fname
    session['lname'] = lname
    session['email'] = email
    session['pas'] =  pas
    session['email_otp'] = code
    return redirect(url_for('public.emailVerifyForRegister'))

@public.route('/verifyEmailAddress', methods=['POST', 'GET'])
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
            return redirect(url_for('public.login_me'))
    return render_template('resigration/emailverify.html')
    

#Here is logic of Login for Users, For those who have already account
@public.get('/login')
def login_me():
    return render_template('resigration/login.html')

@public.post('/login')
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
            return redirect(url_for('public.home'))
        elif (email==i[4]) and (check_password_hash(i[5], pas) == False ):
            flash('Wrong Password try again:- ')
            return redirect(url_for('public.login_me'))
        
        flash("You Don' have Account in website Please Register Youself:- ")
        return redirect(url_for('public.register_me'))
    

@public.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        email = request.form.get('email')
        val = emailOtpSender(email)
        session['otp'] = val
        return redirect(url_for('public.codeVerificationForForgetPassword'))
    return render_template('email.html')


@public.route('/codeVerification', methods=['POST', 'GET'])
def codeVerificationForForgetPassword():
    if request.method == 'POST':
        code = request.form.get('code')
        if int(code) == int(session.get('otp')):
            print('Successful Verify')
            session.pop('otp')
            return redirect('/resetPassword')
        return "code isn't match"
    return render_template('forgetPassCode.html')



@public.route('/resetPassword', methods=['GET', 'POST'])
def resetPass():
    if request.method == 'POST':
        
        pass1 = request.form.get('password')
        pass2 = request.form.get('password2')
        if pass1 == pass2:
            return redirect('/login')
    return render_template('resetPassword.html')

@public.route("/logout")
def logout():
    flash('Logout Successfully See You Again:- ')
    session.pop('uuid', None)
    return redirect('/')
