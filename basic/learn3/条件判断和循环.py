#条件判断
age=3
if age>18 18:
    print('adult')
elif age>=6:
    print('teenager')
else:
    print('kid')

#if语句从下往下判断
if x:
    print('True')
#只要x是非零数值，非空字符串、非空list等，就判断为true，否则为false

#循环
#python的循环有两种，一种是for...in循环，把list或tuple中的每个元素迭代出来
names=['Michael','Bob','Tracy']
for name in names:
    print(name)

list(range(5))#输出[0,1,2,3,4]
#第二种是while循环，只要条件满足，就不断循环，条件不满足时推出循环。比如我们要计算100以内所有奇数之和，可以用while实现：

sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)