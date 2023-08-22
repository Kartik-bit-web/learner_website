from flask import render_template, request, redirect, url_for, Blueprint, session, flash

# Importing sub categories folder and file 
from public_panel.sub_cat.sub_categories import sub_cate

from modules.databaseconnection import mydb

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

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
    name = request.form.get('name')
    email = request.form.get('email')
    pas = request.form.get('password')

#Here is logic of Login for Users, For those who have already account
@public.get('/login')
def login_me():
    return render_template('resigration/login.html')

@public.post('/login')
def post_login():
    email = request.form.get('email')
    pas = request.form.get('pass')
    flash('Incorrect Password or Email Plaese Recheck and try Again:- ')
    return redirect('/login/')

@public.route('/email', methods=['GET', 'POST'])
def email():
    if request.method == 'POST':
        email = request.form.get('email')

        sender_email = 'km8469879@gmail.com'
        receiver_email = email
        subject = 'Test Email'
        x = randint(000000, 999999)
        val = x
        message = 'This is a test email sent from Python. and This is youe OTP: {}'.format(val)

        # Set up the MIME object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # SMTP server settings
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Use 465 for SSL

        # Login credentials
        smtp_username = 'km8469879@gmail.com'
        smtp_password = 'oblgudefvpacblil'

        # Connect to the SMTP server and send the email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Upgrade the connection to secure mode
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print('Error sending email:', str(e))
        finally:
            server.quit()
        return redirect(url_for('public.forget_pass', store=val))
    return render_template('email.html')

@public.route('/forgetPassword/<store>', methods=['GET', 'POST'])
def forget_pass(store):
    if request.method == 'POST':
        code = request.form.get('code')
        if int(code) == int(store):
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



#@public.route('/<int:id>', methods=['GET', 'POST'])
#def sub_cate(id):
#    return render_template('sub_cate.html', )
#
#@public.route('/<int:id>/<int:id2>', methods=['GET', 'POST'])
#def content(id, id2):
#    if request.method == 'POST':
#        ids = request.form['id']
#        sug = request.form['sug']
#
#    error = 'This Page is Being Production. Soon Getting ready for the service...'
#    return render_template('main_content.html')
#
#@public.route("/logout")
#def logout():
#    flash('Logout Successfully See You Again:- ')
#    session.pop('username', None)
#    session.pop('userid', None)
#    return redirect('/')
#