#coding=utf-8
from flask import Flask
from user_views import user_views  # 导入蓝图模块
from datetime import timedelta
import  os

app = Flask(__name__)   #实例化app
app.register_blueprint(user_views)   #加载蓝图
# app.secret_key = 'TE-hufeng'     #设置session-key
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)


if __name__=='__main__':
    config = dict(
        debug=True,
        # host = '0.0.0.0'
    )
    # from werkzeug.contrib.fixers import ProxyFix
    # app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(**config) 