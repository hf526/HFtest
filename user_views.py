from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    session,
)

from IRR.account import login_user
from services.user import user

user_views = Blueprint('user_views',__name__,url_prefix='/')


@user_views.route('/', methods=['GET'])     #主页路由
def index():
        return render_template('index.html',title = 'name')


@user_views.route('/login', methods=['POST'])     #主页其他路由
def login():
    account = login_user()
    u = user()
    print(account)
    return u.user_login(**account)

@user_views.route('/home', methods=['GET'])     #主页其他路由
def home():
    if session.get('username'):
        return render_template('home.html')
    else:
        print(session.get('username'))
        return redirect('')


