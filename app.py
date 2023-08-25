from flask import Flask, render_template

from auth.register import register
from auth.login import login

from public_panel.categories import category
from public_panel.page import page
from public_panel.about_us import about


app = Flask(__name__)
app.secret_key = "406b617254494b333231"
 
#Auth login and Register 
app.register_blueprint(register, url_prefix='/register')
app.register_blueprint(login, url_prefix='/login')

# front Options Categories, Page, about_us
app.register_blueprint(category, url_prefix='/categoires')
app.register_blueprint(page, url_prefix='/page')
app.register_blueprint(about, url_prefix='/about_us')

#Here is website's HOME page, Landing page of website
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')



