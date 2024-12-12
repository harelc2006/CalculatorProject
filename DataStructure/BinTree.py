class BinTree:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, x):
        self.value = x

    def insertLeft(self, x):
        self.left = BinTree()
        self.left.value = x

    def insertRight(self, x):
        self.right = BinTree()
        self.right.value = x

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left.value

    def getRight(self):
        return self.right.value

    def isLeaf(self):
        return self.right is None and self.left is None

    def hasLeft(self):
        return self.left is None

    def hasRight(self):
        return self.right is None
