def toStr(n,base):
    convertString='0123456789ABCDEF'
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]


# 使用栈
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

rStack=Stack()

def toStrStack(n,base):
    convertString='0123456789ABCDEF'
    while n>0:
        if n<base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n=n//base
    res=""
    while not rStack.isEmpty():
        res=res+str(rStack.pop())
    return res

print(toStrStack(10,2))

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

# drawSpiral(myTurtle,100)
# myWin.exitonclick()

# 绘制树

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(100,t)
#     myWin.exitonclick()

# main()

# 绘制三角形
def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree,myTurtle):
    colormap=['blue','red','green','white','yellow','violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree>0:
        sierpinski([points[0],getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[1], getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[2], getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)

def main():
    myTurtle=turtle.Turtle()
    myWin=turtle.Screen()
    myPoints=[[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()

main()
