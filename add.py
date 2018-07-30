import hashlib
from services import user

username = 'admin'
password = 'x1295526817'
print(username, password)
password = ("1295526817" + password).encode('utf-8')  # HA1加密必须是byis类型
md5 = hashlib.md5()  # SHA1加密，实例化
md5.update(password)  # 进行加密
password = md5.hexdigest()
print(username, password)

u = user()

u.add_user(username=username,password=password)