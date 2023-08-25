from flask import Blueprint, render_template

#from modules.databaseconnection import mydb

content = Blueprint('content', __name__, template_folder='templates', static_folder='static')

#this is Child of categories, here is sub categorie's filtered its sub categories

@content.route('/', methods=['GET', 'POST'])
def contents(id):
    print(id)
    return render_template('main_content.html')