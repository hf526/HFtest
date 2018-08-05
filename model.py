import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/test?charset=utf8'
db = SQLAlchemy(app)


class User(db.Model):  #用户表   5个字段（id，用户名，密码，创建时间，更新时间）
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

    def __repr__(self): # 定义打印的类型，打印表名
        return '<User %r>' % self.__tablename__

class Project(db.Model):     #项目表   6个字段（id，项目名，创建人，创建时间，更新时间，user_id）
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key = True)
    project_name = db.Column(db.String(80),unique = True)
    creat_man = db.Column(db.String(80))
    creat_time = db.Column(db.DateTime())
    update_time = db.Column(db.DateTime(), default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id")) #初始化关联 ForeignKey("表名加字段")
    users = db.relationship("User", backref="project")   #建立表关联  db.relationship("model类", backref="表名")


    def __init__(self, project_name,creat_man, user_id,creat_time):
        self.username = project_name
        self.creat_man = creat_man
        self.password = user_id
        self.creat_time = creat_time

    def __repr__(self):
        return '<user %r>' % self.__tablename__





