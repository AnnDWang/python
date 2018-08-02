class Animal(object):
    def run(self):
        print('Animal is running...')

# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# dog=Dog()
# dog.run()
#
# cat=Cat()
# cat.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog,Dog))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())

run_twice(Dog())

#多态

#对扩展开放：允许新增Animal子类
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数

#静态语言VS动态语言
#对于像Java这样的静态语言，如果需要传入Animal类型，传入的必须是Animal类型或者他的子类，否则，将无法调用run方法，
#对于像python这样的动态语言来说，则不一定需要传入Animal类型，我们只需要保证传入的对象有一个run方法就可以了
#这就是动态语言的鸭子类型，并不要求严格的继承体系，一个对象只要看起来像鸭子，走起路来像鸭子，就可以看做是鸭子

