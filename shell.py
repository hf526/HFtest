import  os


os.system('killall -9 uwsgi')
os.system('killall -9 nginx')
os.system('nohup uwsgi uwsgi.ini &')
os.system('\r')
os.system('nohup nginx &')
