from flask import render_template, request, redirect, url_for, Blueprint, session
from functools import wraps

from werkzeug.utils import secure_filename
import os

#def login_required(f):
#    @wraps(f)
#    def wrap(*args, **kwargs):
#        v = session.get('username')
#        if  v == 'km8469879@gmail.com':
#            return f(*args, **kwargs)
#        return redirect('/login/')
#    return wrap

category = Blueprint('category', __name__, template_folder='templates', static_folder='static')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = './static'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@category.route('/', methods=['GET', 'POST'])

def create_cate():
    if request.method == 'POST':
        name = request.form['name']
        file_name = request.files['file']
        if file_name and allowed_file(file_name.filename):
            file = secure_filename(file_name.filename)
            file_name.save(os.path.join(UPLOAD_FOLDER, file))
            return redirect('/category/')
    return render_template('/admin/createCategory.html')

@category.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_cate(id):
    if request.method == 'POST':
        name = request.form['name']
        file_name = request.files['file']
        if file_name and allowed_file(file_name.filename):
            file = secure_filename(file_name.filename)
            file_name.save(os.path.join(UPLOAD_FOLDER, file))

            return redirect('/category/')

    return render_template('/admin/edit_category.html')

@category.route('/delete_category/<int:id>', methods=['GET', 'POST'])
def del_cate(id):

    return redirect('/category/')