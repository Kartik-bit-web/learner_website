from flask import Flask

#from admin_panel.main_admin import admin
#from admin_panel.create_category import category
#from admin_panel.sub_cate import sub_cate
##from admin_panel.contents import contents
#from admin_panel.login.resister import resister
#from admin_panel.login.login import logins

from public_panel.main_page import public


app = Flask(__name__)

app.secret_key = "406b617254494b333231"



app.register_blueprint(public, url_prefix='/')

#app.register_blueprint(admin, url_prefix='/admin')
#
#app.register_blueprint(category, url_prefix='/category')
#
#app.register_blueprint(sub_cate, url_prefix='/sub_cate')
#
#app.register_blueprint(resister, url_prefix='/register')
#
#app.register_blueprint(logins, url_prefix='/login')

#app.register_blueprint(contents, url_prefix='/content')


