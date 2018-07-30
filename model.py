import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
db = SQLAlchemy(app)


class User(db.Model):
#数据库模型，用户表  资料：https://blog.csdn.net/yongsan01/article/details/52205771   https://www.cnblogs.com/FRESHMANS/p/8459716.html
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)           #id 自增主键
    username = db.Column(db.String(10), unique = True)
    password = db.Column(db.String(80))
    creat_time = db.Column(db.DateTime())
    update_time = db.Column(db.DateTime(),default=datetime.datetime.now)


    def __init__(self, username, password,creat_time):
        self.username = username
        self.password = password
        self.creat_time = creat_time

    def __repr__(self): # 定义返回的类型
        return '<User %r>' % self.username

class Project(db.Model):     #项目表
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(80),unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    users = db.relationship("User", backref="project")

    def __init__(self, project_name, user_id,users):
        self.username = project_name
        self.password = user_id
        self.creat_time = users

    def __repr__(self):
        return '<user %r>' % self.name





