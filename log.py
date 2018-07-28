import time,os,inspect

now_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
data_time = time.strftime("%Y-%m-%d",time.localtime())
path = os.path.dirname(os.getcwd())
log_name = '{}\log\{}.txt'.format(path,data_time)


def  log(func):
    def inner(*args, **kwargs):
        fun = func(*args, **kwargs)
        with open(log_name, 'a', encoding='utf-8') as file:
             s = "{} | 函数名：{} | 传入参数：{},{}".format(now_time,func.__name__,args, kwargs)
             print(s)
             file.write(str(s)+"\n")
        return fun
    return inner

