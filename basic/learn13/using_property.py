# 直接检查参数，又可以类似属性这样的简单方式来访问类的变量
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integer!")
        if value < 0 or value >100 :
            raise ValueError("score must between 0 and 100")
        self._score=value

# @property的实现较为复杂，把一个getter方法变成属性，只要加上@property就可以了，此时，property又创建了另一个装饰器@score.setter，负责吧一个setter方法变成属性赋值

s=Student()
s.score=60
print( s.score)
s.score=-10
#定义只读属性，只定义getter方法，不定义setter方法就可以了
