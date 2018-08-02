#面向对象最重要的概念就是class和instance，类是抽象的模板

# class Student(object):
#     pass

#class后紧跟类名，即Student，类名通常是大写开头的单词，仅着这（object），表示该类从哪个类继承下来的，通常，如果没有适合的继承类，就是用object类，这是所有类最终都会继承的类

# bart =Student()

class Student(object):
    def __int__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

#__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以吧各种属性绑定到self，因为self就指向创建的实例本身
#有了__init__方法，在创建实例的时候就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，python解释器会自己把实例变量穿进去
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且调用时不需要传递该参数。除此之外，类的方法和普通方法没有区别

#数据封装

