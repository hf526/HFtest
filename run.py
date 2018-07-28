#coding=utf-8
from flask import Flask

from user_views import user_views  # 导入蓝图模块

app = Flask(__name__)   #实例化app
app.register_blueprint(user_views)   #加载蓝图
app.secret_key = 'TE-hufeng'     #设置session-key



if __name__=='__main__':
    config = dict(
        debug=True,
        # host = '0.0.0.0'
    )
    app.run(**config)