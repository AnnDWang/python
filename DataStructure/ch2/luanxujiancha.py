# 乱序字符检查的例子
# https://facert.gitbooks.io/python-data-structure-cn/2.%E7%AE%97%E6%B3%95%E5%88%86%E6%9E%90/2.4.%E4%B8%80%E4%B8%AA%E4%B9%B1%E5%BA%8F%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A3%80%E6%9F%A5%E7%9A%84%E4%BE%8B%E5%AD%90/
# 乱序字符串是指一个字符串只是另一个字符串的重新排列
# 比如：'heart'和'earth'就是乱序字符
# 假设所讨论的两个字符串具有相等的长度，并且由26个小写字母集合组成

# 解法1：检查
# 检查第一个字符串是不是出现在第二个字符串中
# 如果可以检验到每一个字符，那这两个字符串一定是乱序
# 可以通过None替换字符来了解一个字符是否完成检查
# 但是，由于Python字符串是不可变的，
# 所以第一步是将第二个字符串转换为列表
# 检查第一个字符串中的每个字符是否存在于第二个列表中
# 如果存在，替换成None

def anagramSolution1(s1,s2):
    alist=list(s2)

    pos1=0
    stillOK=True

    while pos1<len(s1) and stillOK:
        pos2=0
        found=False
        while pos2<len(alist) and not found:
            if s1[pos1]==alist[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            alist[pos2]=None
        else:
            stillOK=False

        pos1=pos1+1
    return stillOK

# print(anagramSolution1('abcd','dccab'))

# 解法2：排序和比较
# 即使s1，s2不同，它们都是由完全相同的字符组成的
# 按顺序排列每个字符串
# 如果两个字符串相同
# 那么这两个字符串就是乱序字符串
def anagramSolution2(s1,s2):
    alist1=list(s1)
    alist2=list(s2)

    alist1.sort()
    alist2.sort()

    pos=0
    matches=True

    while pos<len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            matches=False
    return matches

# print(anagramSolution2('abdef','abefd'))

# 解法3：穷举法
# 对于乱序检测，
# 可以生成s1的所有乱序字符串列表，然后查看是不是有s2，
# 这种方法有困难在于可能的字符串有n!种
# 不是很好地解决方案

# 解法4：计数和比较
# 利用两个乱序字符串具有相同数目的a,b,c等字符的事实。
# 首先计算的是每个字母出现的次数
# 用一个长度为26的列表
# 每个可能的字符占一个位置
# 每次看到一个特定的字符，就增加该位置的计数器
# 如果两个列表的计数器一样，则字符串为乱序的字符串
def anagramSolution4(s1,s2):
    c1=[0]*26
    c2=[0]*26

    for i in range(len(s1)):
        # ord() 函数是 chr() 函数（对于8位的ASCII字符串）
        # 或 unichr() 函数（对于Unicode对象）的配对函数，
        # 它以一个字符（长度为1的字符串）作为参数，
        # 返回对应的 ASCII 数值，或者 Unicode 数值，
        # 如果所给的 Unicode 字符超出了你的 Python 定义范围，
        # 则会引发一个 TypeError 的异常。
        pos=ord(s1[i])-ord('a')
        c1[pos]=c1[pos]+1

    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        c2[pos]=c2[pos]+1

    j=0
    stillOK=True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j=j+1
        else:
            stillOK=False
    return stillOK

print(anagramSolution4('apple','pleap'))