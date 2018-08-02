#可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等
#一类是generator，包括生成器和带yield的generator function
#这类可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
isinstance([],Iterable)#True
isinstance({},Iterable)#True
isinstance('abc',Iterable)#True
#可以被next（）调用并不断返回下一个值得对象称为迭代器
#生成器都是Iterator对象，，但是list、dict、str虽然是Iterable。却不是Iterator
#把list、dict等Iterable变成Iterator可以使用iter()函数
isinstance(iter([]),Iterator)#True
#为什么list等不适Iterator？因为python的Iterator对象表示的是一个数据流，Iterator对象可以被next()调用并不断返回下一个数据，知道没有数据时排除StopIteration错误。可以把这个数据流看做是一个有序序列，但是我们却不能提前知道序列的长度，只能不断通过next（）函数实现按需计算下一个数据，Iterator的计算是惰性的，只有在需要返回下一个数据时才会计算
#Iterator甚至可以表示一个无线大的数据流，如全体自然数，而使用list是永远不可能存储全体自然数的、
