import  os



os.system('')
os.system('source venv/bin/activate')
os.system('killall -9 uwsgi')
os.system('killall -9 nginx')
os.system('nohup uwsgi uwsgi.ini &')
os.system('\r')
os.system('nohup nginx &')
