#排序也是在程序中常用到的算法
#python内置的sorted()函数可以对list进行排序
sorted([36,5,-12,9,-21])
#sorted也是一个高阶函数，还可以接收一个key函数来实现自定义的排序，例如按照绝对值大小排序
sorted([36,5,-12,9,-21],key=abs)

#key制定的函数将作用域list的每一个元素上，并根据key函数返回的结果进行排序。

#要进行反向排序，需要传入参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
#['Zoo', 'Credit', 'bob', 'about']
