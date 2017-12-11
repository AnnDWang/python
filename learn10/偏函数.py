#python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
#在介绍函数参数时，通过设定参数的默认值，可以降低函数调用的难度，而偏函数也可以做到这一点
#int()函数可以吧字符串转换为整数，当仅仅传入字符串时，int()函数默认按照十进制转换
int('12345') #输出12345
#但是int函数还提供额外的base参数，默认值为10，如果传入base参数，就可以做N进制的转换
int('12345',base=8) #输出5349
int('12345',16)#输出74565

#如果需要大量的二进制字符串，每次都传入int(x,base=2)很麻烦，可以定义一个int2()的函数，默认base=2
def int2(x,base=2):
    return int(x,base)

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2()
import functools
int2=functools.partial(int,base=2)

#简单来说，functools.partial的作用就是把一个函数的某些参数固定（即设置默认值），返回一个新的函数，调用这个新的函数会更简单，注意到上面的新的int2函数，仅仅是吧base
#参数重新设定默认值为2，但也可以在函数调用时传入其他值

#创建偏函数时，实际上可以接受函数对象、*args和**kw这三个参数

int2 = functools.partial(int, base=2)
#就是：
kw = { 'base': 2 }
int('10010', **kw)

max2 = functools.partial(max, 10)
#就是：
max2(5, 6, 7)
#等价于
args = (10, 5, 6, 7)
max(*args)