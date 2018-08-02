#函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2015-3-25')

f=now

f()
#输出 2015-3-25

#函数对象有一个__name__属性，可以拿到函数的名字：
now.__name__
#'now'
f.__name__
#'now'

#现在，假设我们要增强now的功能，在函数调用前后自动打印日志，又不希望修改now函数的定义，这种在代码运行期间动态增加功能的方式，称之为装饰器

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-3-24')

now=log(now)