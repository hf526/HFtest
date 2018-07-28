#coding=utf-8
import hashlib  # 进行数据加密模块

from model import User, db


def add_user(**kwargs):
    username = kwargs["username"]
    password = ("1295526817"+kwargs["password"]).encode('utf-8')             #HA1加密必须是byis类型
    md5 = hashlib.md5()                                                      #SHA1加密，实例化
    md5.update(password)
    u = User(username, md5.hexdigest())                                     #存储数据库
    db.session.add(u)                                                       #添加数据库
    db.session.commit()                                                     #提交事务

