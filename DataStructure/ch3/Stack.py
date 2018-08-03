class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

s=Stack()



# 检测括号(是否匹配
def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=='(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()

        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# 检测符号[]{}()匹配
def parChecker1(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                if not matched(top,symbol):
                    balanced=False
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matched(open,close):
    opens='([{'
    closers=')]}'
    return opens.index(open)==closers.index(close)


# print(parChecker1('{[][()]()}'))

# 除2算法
def divideBy2(decNumber):
    remstack=Stack()
    while decNumber>0:
        rem=decNumber%2
        remstack.push(rem)
        decNumber=decNumber//2
    binString=""
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())
    return binString

# print(divideBy2(233))

# 十进制数和 2-16之间的任何基数
def baseConverter(decNumber,base):
    digits="0123456789ABCDEF"
    remstack=Stack()
    while decNumber>0:
        rem=decNumber%base
        remstack.push(rem)
        decNumber=decNumber//base

    newString=""
    while not remstack.isEmpty():
        newString=newString+digits[remstack.pop()]
    return newString
# print(baseConverter(233,2))
# print(baseConverter(233,16))

# 中缀表达式转后缀
# 使用一个名为prec的字典来保存操作符的优先级
# 这个点将每个运算符映射到一个整数，可以与其他运算符的优先级（是固体部分整数3，2，1）进行比较
# 左括号被赋予最低的值，这样，与其进行比较的任何运算符都将具有更高的优先级，将被放置在它的顶部
def infixToPostfix(infixexpr):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    opStack=Stack()
    postfixList=[]
    tokenList=infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in "0123456789":
            postfixList.append(token)
        elif token=='(':
            opStack.push(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else:
            while(not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

# 计算后缀表达式的值
def postfixEval(postfixExpr):
    operandStack=Stack()
    tokenList=postfixExpr.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2=operandStack.pop()
            operand1=operandStack.pop()
            result=doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op,op1,op2):
    if op=="*":
        return op1*op2
    elif op=='/':
        return op1/op2
    elif op=='+':
        return op1+op2
    else:
        return op1-op2

print(postfixEval('7 8 + 3 2 + /'))
