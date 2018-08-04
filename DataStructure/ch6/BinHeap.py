
# 整个二叉堆可以由单个列表表示
# 一个空的二叉堆有一个单一的0作为heapList的第一个元素，这个0只是放在那里
# 用于以后简单的整数除法
class BinHeap:
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0

    # 在树中向上遍历一个新项
    # 因为它需要去维护堆属性
    # 可以通过使用简单的整除法来计算任意节点的父节点
    def precUp(self,i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize=self.currentSize+1
        self.percUp(self.currentSize)

    # 删除堆分为两步，首先，通过获取列表中的最后一个项并将其移动到根位置来恢复根项
    # 保持堆结构的属性
    # 但是二叉堆的顺序属性已经被破坏
    # 接下来，通过将新的根节点沿着树向下推到正确位置来恢复堆顺序属性
    def percDown(self,i):
        while (i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc

    def minChild(self,i):
        if i*2+1>self.currentSize:
            return i*2
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval=self.heapList[1]
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize=self.currentSize-1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentSize=len(alist)
        self.heapList=[0]+alist[:]
        while (i>0):
            self.percDown(i)
            i=i-1
bh=BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())

print(bh.insert(4))

