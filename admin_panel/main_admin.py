from flask import render_template, request, redirect, url_for, Blueprint, session
from functools import wraps

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

#def login_required(f):
#    @wraps(f)
#    def wrap(*args, **kwargs):
#        v = session.get('username')
#        if  v == 'km8469879@gmail.com':
#            return f(*args, **kwargs)
#        return redirect('/login/')
#    return wrap

@admin.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('admin/adminindex.html')