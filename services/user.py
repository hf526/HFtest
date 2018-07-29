#coding=utf-8
from flask import jsonify
from model import User, db
import json


class user():
    def __init__(self):
        pass
    def add_user(self,**kargs):
        u = User( kargs["username"], kargs["password"] )                                     #存储数据库
        db.session.add(u)                                                       #添加数据库
        db.session.commit()                                                     #提交事务

    def user_login(self,**kargs):
        print(kargs)
        self.username=kargs['username']
        self.password=kargs['password']
        try:
            U = User.query.filter_by(username=self.username).first()
            if self.password == U.password:
                return jsonify({"type":1,"msg":"登录成功"})
            else:
                return jsonify({"type":2,"msg":"密码错误"})
        except:
            return jsonify({"type":3,"msg":"账户不存在"})





