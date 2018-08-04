# # 用列表来表示树
# myTree=['a',# root
#         ['b',# left subtree
#          ['d',[],[]],
#          ['e',[],[]]
#          ],
#         ['c',# right subtree
#          ['f',[],[]],
#          []
#          ]
#         ]
#
# def BinaryTree(r):
#     return [r,[],[]]
#
# # 要插入一个左子节点，
# # 首先获得与当前子节点对应的列表（可能为空），
# # 然后添加新的左子树
# # 添加旧的左子树作为新子节点的左子节点
# # 这允许我们在任何位置将新节点拼接到树中
# def insertLeft(root,newBranch):
#     t=root.pop(1)
#     if len(t)>1:
#         root.insert(1,[newBranch,t,[]])
#     else:
#         root.insert(1,[newBranch,[],[]])
#     return root
#
# def insertRight(root,newBranch):
#     t=root.pop(2)
#     if len(t)>1:
#         root.insert(2,[newBranch,[],t])
#     else:
#         root.insert(2,[newBranch,[],[]])
#     return root
#
# def getRootVal(root):
#     return root[0]
#
# def setRootVal(root,newVal):
#     root[0] = newVal
#
# def getLeftChild(root):
#     return root[1]
#
# def getRightChild(root):
#     return root[2]

class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

# r=BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

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


def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=='(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+','-','*','/',')']:
            currentTree.setRootVal(int(i))
            parent=pStack.pop()
            currentTree=parent
        elif i in ['+','-','*','/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i==')':
            currentTree=pStack.pop()
        else:
            raise ValueError
    return  eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")

import operator

def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,
           '*':operator.mul,'/':operator.truediv}
    leftC=parseTree.getLeftChild()
    rightC=parseTree.getRightChild()

    if leftC and rightC :
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
print(evaluate(pt))

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree!=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

inorder(pt)

