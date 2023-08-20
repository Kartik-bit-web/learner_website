from flask import render_template, request, Blueprint, session, redirect
from werkzeug.utils import secure_filename
from functools import wraps

import os

sub_cate = Blueprint('sub_cate', __name__, template_folder='templates', static_folder='static')

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        v = session.get('username')
        if  v == 'km8469879@gmail.com':
            return f(*args, **kwargs)
        return redirect('/login/')
    return wrap


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = './static/sub_cate'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@sub_cate.route('/', methods=['GET', 'POST'])
@login_required
def sub_category():
    if request.method == 'POST':
        name = request.form.get('name')
        lists = request.form.get('list')
        file = request.files['file']
        if file and allowed_file(file.filename):
            file_it = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, file_it))

    return render_template('admin/sub_category.html', use={'x':None, 'y':None})
