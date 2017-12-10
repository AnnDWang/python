#当我们在传入函数时，有时候不需要显示定义函数，直接传入匿名函数更方便
list(map(lambda  x:x*x,[1,2,3,4,5,6]))

#通过对比可以看出，匿名函数lamaba x:x*x实际上就是
def f(x):
    return x*x

#关键字lamba表示匿名函数，冒号前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
#用匿名函数的好处是，函数没有名字，不必担心函数名冲突。
#此外，匿名函数也是一个函数对象，也可以吧匿名函数复制给一个变量，在利用变量来调用该函数。
f=lambda x:x*x
#也可以吧匿名函数作为返回值返回
def build(x,y):
    return lambda :x*x+y*y