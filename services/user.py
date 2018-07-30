#coding=utf-8
from flask import jsonify,session
from model import User, db
import json,time


class user():
    def __init__(self):
        pass
    def add_user(self,**kargs):
        print(kargs)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        u = User( kargs["username"], kargs["password"],create_time )                                     #存储数据库
        db.session.add(u)                                                       #添加数据库
        db.session.commit()                                                     #提交事务

    def user_login(self,**kargs):
        print(kargs)
        self.username=kargs['username']
        self.password=kargs['password']
        print(self.username,self.password)
        try:
            U = User.query.filter_by(username=self.username).first()
            print('用户密码',self.password)
            print('数据库密码',U.password)
            if self.password == U.password:
                session['username'] = 'success'
                return jsonify({"code":1,"msg":"登录成功"})
            else:
                return jsonify({"code":2,"msg":"密码错误"})
        except:
            return jsonify({"code":3,"msg":"账户不存在"})





