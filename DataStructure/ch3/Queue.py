# https://facert.gitbooks.io/python-data-structure-cn/3.%E5%9F%BA%E6%9C%AC%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/3.12.Python%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97/
from numpy import *

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# 模拟烫手山芋

def hotPotato(namelist,num):
    simqueue=Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

# 模拟打印机

# 打印机类
# 需要跟踪当前是否有任务
# 如果有，则处于忙碌状态
# 并且可以从任务的页数计算所需的时间
# 构造函数允许初始化每分钟页面的配置
# tick方法将内部定时器递减直到打印机设置为空闲
class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0

    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate

# Task类：表示单个打印任务
# 创建任务时，随机数生成器提供1-20页的长度
# 每个任务还有保存一个时间戳用于计算等待时间
# 此时间戳将表示任务被创建并放置到打印机队列中的时间，
# 可以使用waitTime方法来检索在打印开始之前队列中花费的时间
import random
class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp

# 模拟打印机队列
# PrintQueue对象时现在队列ADT的一个实例
# newPrintTask决定是否创建一个新的打印任务
# 再次选择使用随机模块的randrange函数返回1到180之间的随机整数
# 打印任务每180秒到达一次
# 通过从随机整数的范围中任意选择，我们可以模拟这个随机事件
# 模拟功能允许我们设置打印机的总时间和每分钟的页数

def simulation(numSeconds,pagesPerMinute):
    labprintet=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprintet.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprintet.startNext(nexttask)

        labprintet.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False

for i in range(10):
    simulation(3500,5)





