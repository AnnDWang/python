#python是动态语言，根据类创建的实例可以任意绑定属性，给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
    def __init__(self,name):
        self.name=name
s=Student('Bob')
s.score=90

#在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将会屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称
#访问到的是类属性
