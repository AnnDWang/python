#使用list和tuple

#list
#python内置的一种数据类型是列表list。list是一种有序的集合，可以随时添加额删除其中的元素。
classmates=['Michael','Bob','Tracy']
classmates #输出['Michael','Bob','Tracy']
#变量classmates就是一个list。用len()可以获得list元素个数
len(classmates)#输出3
#用索引来访问list中每一个位置的元素，索引从0开始
#索引超过范围时，会报indexerror错误。
#要获取最后一个元素，还可以用-1作为索引
#以此类推，-2，-3，-4获取倒数第二个第三个第四个。
#list是一个可变的有序表，所以可以往list中追加元素到末尾
classmates.append('Adam')
#也可以把元素插入到指定位置，比如说索引号为1的位置：
classmates.insert('Jack',1)
classmates#输出['Michael','Jack','Bob','Tracy','Adam']
#要删除list末尾的元素，用pop()方法
classmates.pop()#输出‘Adam’
classmates#输出['Michael','Jack','Bob','Tracy']
#要删除指定位置的元素，用pop(i)方法，i是索引位置
classmates.pop(1)#输出jack
#要把某个元素换成别的元素，可以直接赋值给对应的索引位置：
classmates[1]='Sarah'
classmates#输出：['Michael','Sarah','Tracy']
#list中的元素的数据类型也可以不同，比如：
L=['Apple',123,True]
#list的元素也可以是另一个list
#如果list中一个元素也没有，就是一个空list，长度是0


#tuple
#另一种有序列表叫做元祖，tuple。和list非常类似，但是tuple一旦初始化就不能修改
#tuple没有append()insert()这样的方法，可以读取数据，但不能赋值。tuple不可变，代码更加安全。
#tuple在定义的时候，元素必须被确定，如果要定义只有一个元素的tuple
t=(1)
t#输出1
#定义的不是tuple，而是1，括号()既可以表示tuple，又可以表示数学公式中的小括号。python规定，按小括号计算，计算结果为 1
t=(1,)#以这种方式来消除歧义
