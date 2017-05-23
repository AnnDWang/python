#字符和编码

#字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。
#因为计算机只能处理数字，如果要处理文本，就必须把文本转换为数字才能处理。最早的计算机在设计时
#采用8个比特（bit）作为一个字节，所以，一个字节能表示的最大整数就是255
#二进制11111111=十进制255，如果要表示更大的整数，就必须用更多的字节

#由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码

#但要处理中文显然一个字节是不够的，至少需要两个字节，还不能和ASCII编码冲突，所以中国定制了GB2312编码，日本日文Shift_JIS，韩文Euc-kr。各国有各国的标准，在多语言混合的文本中，显示出来会有乱码。
#因此unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会有乱码问题了。
#Unicode通常用两个字节表示一个字符。
#如果同意成Unicode编码，乱码问题小时，但是如果文本全都是英文，用Unicode编码需要多一倍的存储空间，在存储和传输上十分不划算。
#本着节约的精神，出现了吧Unicode编码转化为“可变长编码”的UTF-8，UTF-8编码把一个Unicode字符根据不同的数据大小编码成1-6个字节
#常用英文字母一个字节，汉子通常为3个字节，生僻字符会被编码成4-6个字节。

#我们可以总结一下现在计算机系统通用的字符编码工作方式：
#在计算机内存时，同意使用unicode编码，当需要保存到硬盘或者需要传输的时候，转化为UTF-8编码。

#python字符串

#在最新的python3版本中，字符串是以unicode编码的，也就是说，python的字符串支持多语言
#对于单个字符的编码，python提供了ord()函数后去字符的整数表示，chr()函数把编码转换为对应的字符
ord('A') #输出：65
ord('中') #输出20013

#如果知道字符的整数编码，还可以用十六进制：
'\u4e2d\u6587' #输出：’中文‘
#两种写法完全等价
#由于python的字符串类型是str，在内存中以unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#python对bytes类型的数据用带b前缀的单引号或双引号表示：
x=b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然是内容显示和前者一样，但bytes的每个字符都只占一个字节。
#以unicode表示的str通过encode()方法可以为编码制定的bytes，例如：
'ABC'.encode('ascii') #输出：b'ABC'
'中文'.encode('utf-8') #输出：b'\xe4\xb8\xad\xe6\x96\x87'
#纯英文的str可以用ASCII编码为bytes，内容是一样的
#在bytes中，无法显示为ASCII字符的字节，用\x##显示
#如果我们才能够网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str。就需要用decode()方法
b'ABC'.decode('ascii') #输出'ABC'
#要计算str包含多少个字符，可以用len()函数
len('ABC') #输出：3
len('中文') #输出：2
#len()函数计算str的字符数，bytes，len()函数就计算字节数
#格式化
#最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似’亲爱的xxx你好！你xx月的话费是xxx，余额是xx‘之类的字符串。xxx的内容都是根据变量变化的。

'Hello,%s' % 'world'#输出’hello，world‘
'Hi, %s, you have $%d.' % ('Michael',1000000)
'Hi,Michael,you have $1000000'
#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%？占位符，后跟跟几个变量或值，如果只有一个%？，括号可以省略。

