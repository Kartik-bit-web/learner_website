from flask import Flask, Blueprint, render_template

from modules.databaseconnection import mydb

from public_panel.sub_cat.real_content.content import content

sub_cate = Blueprint('sub_cate', __name__, template_folder='templates', static_folder='static')

#this is Child of categories, here is sub categorie's filtered its sub categories
sub_cate.register_blueprint(content, url_prefix="/name")
@sub_cate.route('/<int:id>', methods=['GET', 'POST'])
def sub_cat(id):
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM sub_categories WHERE categories_id = {}'.format(int(id)))
    x = cursor.fetchall()
    print(x)
    return render_template('sub_cate.html', x=x)