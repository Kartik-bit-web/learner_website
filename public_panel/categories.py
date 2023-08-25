from flask import Blueprint, render_template
# Importing sub categories folder and file 
from .sub_cat.content import content

from modules.databaseconnection import mydb

category = Blueprint('category', __name__, template_folder='templates', static_folder='static')
#Here is Categories option and its sub category, sub category has different location for more productive

category.register_blueprint(content, url_prefix='/<int:id>')

@category.route('/', methods=['GET', 'POST'])
def category_me():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM categories')
    x = cursor.fetchall()
    return render_template('category.html', x=x)

@category.route('/<int:id_f>', methods=['GET', 'POST'])
def sub_cat(id_f):
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM sub_categories WHERE categories_id = {}'.format(int(id_f)))
    x = cursor.fetchall()
    return render_template('sub_cate.html', x=x)
