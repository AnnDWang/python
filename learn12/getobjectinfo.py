print(type(123))

#dir函数返回一把包含字符串的list，可以获得一个对象所有属性和方法
print(dir(123))

print('ABV'.lower())

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：