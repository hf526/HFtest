from flask import (
    request,
)
import hashlib  # 进行数据加密模块

def login_user():
    # username = request.form["username"]
    # password = request.form["password"]
    # username = request.args.get("username")
    # password = request.args.get("password")
    username = 'admin'
    password = 'x1295526817'
    print(username, password)
    password = ("1295526817" + password).encode('utf-8')  # HA1加密必须是byis类型
    md5 = hashlib.md5()  # SHA1加密，实例化
    md5.update(password)   # 进行加密
    password = md5.hexdigest()
    print(username, password)
    user = dict (
        username = username,
        password = password,
    )
    return user


login_user()