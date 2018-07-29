from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for
)

from IRR.account import login_user
from services.user import user

user_views = Blueprint('user_views',__name__,url_prefix='/')


@user_views.route('/', methods=['GET'])     #主页路由
def index():
        return render_template('index.html')


@user_views.route('/login', methods=['POST'])     #主页其他路由
def other_index():
    account = login_user()
    u = user()
    print(account)
    return u.user_login(**account)


# @user_views.route('/sign')    #注册路由
# def sign():
#     # user_message = sign_user()
#     # add_user(user_message)
#     # return "errot"
#     return render_template('home.html')
