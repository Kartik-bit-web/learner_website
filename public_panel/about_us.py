from flask import Blueprint, render_template
from modules.databaseconnection import mydb


about = Blueprint('about', __name__, template_folder='templates', static_folder='static')

#Here is About section for user to content for a problem or can content directly to support team 
@about.route('/', methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html')