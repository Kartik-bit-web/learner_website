import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

def otpgen():
    return randint(000000, 999999)

def emailOtpSender(email):
    sender_email = 'km8469879@gmail.com'
    receiver_email = email
    subject = 'Test Email'
    val = otpgen()
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
    return val