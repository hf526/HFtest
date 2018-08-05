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


@user_views.route('/', methods=['GET'])     #首页路由
def index():
        return render_template('index.html')


@user_views.route('/login', methods=['POST'])     #登录API
def login():
    account = login_user()
    u = user()
    return u.user_login(**account)

@user_views.route('/home', methods=['GET'])     #主页其他路由
def home():
    if session.get('username'):
        return render_template('home.html')
    else:
        return render_template('index.html')


