#继承可以有很多层次
#以动物为例，采用多重继承，主要的类层次按照哺乳动物和鸟类设计

class Animal(object):
    pass
# 大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

# 现在要给动物加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print("running...")

class Flyable(object):
    def fly(self):
        print("flying...")

class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

# 通过多重继承，一个子类可以同时获得多个父类的所有功能

# 在设计类的继承关系时，通常，主线都是单一继承下来的，如果需要混入额外的功能，使用多重继承实现。


