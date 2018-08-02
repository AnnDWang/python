#切片
#取一个list或tuple的部分元素是很常见的操作
#取前三个元素，可以直接取值或者循环获取元素，但是循环非常繁琐，可以使用切片
L[0:3]
#从索引0开始取，知道索引3位置，但不包括索引3.即0，1，2
#也可以倒数
L[-2:-1]

L=list(range(100))
L[:10]#取前10个数
L[-10:]#取后10个数
L[::5]#每5个取一个
L[:]#原样复制一个
#tuple也是一种list，tuple也可以用切片操作，操作的结果也是tuple
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list货tuple，这种遍历我们成为迭代
#在python中，迭代是通过for...in来完成的，python的for循环可以用在list或tuple对象还可以作用在其他科迭代对象上。
#生成器
#通过列表生成式，我们可以直接创建一个列表，但是受内存限制，列表容量肯定是有限的。如果列表元素可以通过某种算法推算出来，我们可以在循环过程中不断推算出后续的元素，这样不必创建完整的list从而节省大量的空间，在python中，这种一边循环一边计算的机制，称为生成器:generator。
g=(x*x for x in range(10))
#如果要一个一个打印出g的每个元素，可以通过next（）
next(g)#0
next(g)#1
next(g)#4
#正确方法使用for循环。generator也是可迭代对象：
for n in g:
    print(n)
#有些用列表生成式写不出来，但是可以用函数打印出来。
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
#仔细观察，可以看出fib函数事实上定义了斐波那契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator，只需要print(b)改为yield b就可以了：
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
        return 'done'
#这是定义yield的另一种方法。如果一个函数定义中包含了yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
f=fib(6)
f #<generator object fib at 0x104feaaa0>
#这里，最难理解的就是generator和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，每次调用next()执行，遇到yield返回，再次执行时从上次返回yeild语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
#调用改generator时，首先生成一个generator对象，然后用next()不断获得下一个返回值：
o=odd()
next(o) #step 1 1
next(o) #step 2 3
next(o) #step 3 5
#回到fib的例子，我们在循环过程中不断调用yield，就会不断中断，当然要给循环设置一个条件来推出循环，不然会产生一个无限数列出来。
#用for循环调用generator时，发现拿不到generator的return语句的返回值，如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib(6)
while True:
    try: 
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
#Generator return value: done