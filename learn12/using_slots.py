#正常情况下，当我们定义了一个class，创建了一个class的实例之后，我们可以给该实例绑定任何属性和方法，
#这就是动态语言的灵活性
class Student(object):
    pass
#可以给实例动态绑定属性和方法
#如果想给所有的实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
    self.score=score

Student.set_score=set_score

#如果想要限制实例的属性，比如只允许对Student实例添加name和age属性
#为了达到限制的目的，python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name','age')#用tuple定义允许绑定的属性名称

s=Student()
s.name='Michael'
s.age=25
s.score=99
#score没有放到slots中，所以不能绑定score属性
#使用slots属性需要注意，slots定义的属性仅对当前类实例起作用，对继承的子类不起作用

class GraduateStudent(Student):
    pass
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__