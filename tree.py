class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNodeVal):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def getLeftChild(self):
        return self.leftChild
               
    def insertRight(self,newNodeVal):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNodeVal)
        else:
            t = BinaryTree(newNodeVal)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild 
    
    def getRootVal(self):
        return self.key

    def setRootVal(self, Obj):
        self.key = Obj
    
    def __str__(self):
        if self.leftChild:
            leftChild = self.leftChild
        else:
            leftChild = ''
        if self.rightChild:
            rightChild = self.rightChild
        else:
            rightChild = ''
        return f'{self.key}[{leftChild}][{rightChild}]'

if __name__ == '__main__':
    r = BinaryTree('a')
    print(r)
    r.insertLeft('b')
    r.insertRight('c')
    print(r)
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    print(r)
    print(r.getRootVal())
    print(r.getLeftChild())
    print(r.getRightChild())