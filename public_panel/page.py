from flask import Blueprint, render_template
from modules.databaseconnection import mydb


page = Blueprint('page', __name__, template_folder='templates', static_folder='static')
#Here is Jst like blog page where user can ask it's problems and shre their Idea's, and keep updating to user for this website
@page.route('/', methods=['GET', 'POST'])
def page_us():
    return render_template('pages.html')