# python 内建了map()和reduce()函数

def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
list(r)
#[1,4,9,16,25,36,49,64,81]

list(map(str,[1,2,3,4,5,6,7,8,9]))

from functools import reduce

#reduce把一个函数作用在一个序列[x1,x2,x3...]上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

def add(x,y):
    return x+y
reduce(add,[1,3,5])

def fn(x,y):
    return  x*10+y

reduce(fn,[1,3,5,7,9])#13579

#把str转int

def char2num(s):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

reduce(fn,map(char2num,'13579'))

#str转int
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))


#用lambda函数简化
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

