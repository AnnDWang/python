#在class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑
#但是从之前的代码来看，外部代码还是可以自由修改一个实例的name、score等属性。
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线，在Python中，实例的变量名如果以__开头，就变成了一个私有变量
#只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


bart=Student('Bart Simpson',59)

#需要注意的是，在Python中，变量名类似__xx__的，也就是以双下划线开头，并且以双下划綫结尾的，是特殊变量
#特殊变量是可以直接访问的，不是私有变量，所以不能用__name__,__score__这样的变量名

