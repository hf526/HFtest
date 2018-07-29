import  os

os.system('uwsgi --reload uwsgi.ini &')
os.system('nginx -s reload')
