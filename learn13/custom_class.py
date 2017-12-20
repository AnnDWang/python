class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'student object (name:%s)'% self.name
    __repr__=__str__
print(Student('ann'))
Student('ann')

#直接显示变量调用的不是__str__ 而是__repr__，两者的区别是__str__返回用户看到的字符串，__repr__返回程序开发者看到的字符串，后者是为调试服务的

# 如果一个类想被用于for...in循环，类似list或tuple那样，必须实现一个_iter__方法，该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1 #初始化两个计数器
    def __iter__(self):
        return self #实例本社就是迭代对象，因此返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100: #退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

# 要像list那样按照下标取出元素，需要实现__getitem__方法
class Fib(object):
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
print(f[0])

# 正常情况下，当我调用类的方法或者属性时，如果不存在，就会报错，
class Student(object):
    def __init__(self):
        self.name='Michael'

s=Student()
print(s.name)
# print(s.aa)

# 要避免这个错误，除了可以加上一个score属性外，还可以写一个__getattr_方法，动态返回一个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
# 只有在没有找到属性的情况下，才调用__getattr__，比如name，就不会在__getattr__中查找

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用，能不能直接在实例本身上调用呢？任何类只需要定义一个__call__方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print("My name is %s" % self.name)

s=Student('ss')
s()

# __call__()还可以定义参数，对实例直接进行直接调用就好比对一个函数进行调用一样，所以完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没有什么根本区别

print(callable(Student()))
#判断一个函数是否可以调用