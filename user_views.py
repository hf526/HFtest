from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for
)

from IRR.sign import sign_user
# from services.index_service import add_user

user_views = Blueprint('user_views',__name__,url_prefix='/')


@user_views.route('/', methods=['GET'])     #主页路由
def index():
        return render_template('index.html',title = '个人工具网')


@user_views.route('/<name>', methods=['GET'])     #主页其他路由
def other_index(name):
    if name == 'register':
        return render_template('index.html', title='注册')
    elif name == 'login':
        return render_template('index.html', title='登录')
    else:
        return redirect(url_for('index'))


# @user_views.route('/sign')    #注册路由
# def sign():
#     # user_message = sign_user()
#     # add_user(user_message)
#     # return "errot"
#     return render_template('home.html')
