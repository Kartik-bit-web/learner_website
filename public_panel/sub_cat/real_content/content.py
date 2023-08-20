from flask import Flask, Blueprint, render_template

content = Blueprint('content', __name__, template_folder='templates', static_folder='static')

#this is Child of categories, here is sub categorie's filtered its sub categories

@content.route('/content', methods=['GET', 'POST'])
def contents():
    return render_template('main_content.html')