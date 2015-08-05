# AVL tree helper - no interfaces in Python?
class AVL_help:
    def __init__(self,val,left,right,parent):
        # B.C. none for all
        self.left = left
        self.right = right
        self.parent = parent # this is a pointer, right??
        self.data = val
        self.lheight = 0
        self.rheight = 0

    def rotateLeft(self):
        # REQUIRE self.parent is not None, self.parent.right == self
        self.parent.right = self.left
        if self.parent.right:
            self.parent.right.parent = self.parent
        self.left = self.parent
        self.parent = self.left.parent
        self.left.parent = self 
        if self.parent:
            self.parent.left = self

    def rotateRight(self):
        # REQUIRE self.parent is not None, self.parent.left == self
        self.parent.left = self.right
        if self.parent.left:
            self.parent.left.parent = self.parent
        self.right = self.parent
        self.parent = self.right.parent
        self.right.parent = self
        if self.parent:
            self.parent.right = self

    def adjustHeightUp(self,dh):
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.lheight += dh
                self.parent.adjustHeightUp(dh)
            else:
                self.parent.rheight += dh
                self.parent.adjustHeightUp(dh)

    def root(self):
        if self.parent == None:
            return self
        else:
            return self.parent.root()
    
    def insert(self,x):
        if x == self.data:
            return
        else:
            if x > self.data:
                if self.right is None:
                    self.right = AVL_help(x,None,None,self)
                    self.rheight += 1
                else:
                    self.right.insert(x)
                    self.rheight += 1
            else:
                if self.left is None:
                    self.left = AVL_help(x,None,None,self)
                    self.lheight += 1
                else:
                    self.left.insert(x)
                    self.lheight += 1
            
            # invariant of abs(lheight-rheight) <= 1 may be broken
            # could do "pattern match" rebalancing, use "balance factor"
            if self.lheight-self.rheight > 1:
                if self.left.lheight > self.left.rheight:
                    print("right rotate")
                    self.left.rotateRight()
                    self.parent.rheight += 1
                    self.lheight -= 2
                    self.parent.adjustHeightUp(-1)
                else:
                    print("double right rotate")
                    self.left.right.rotateLeft()
                    self.left.rotateRight()
                    self.parent.adjustHeightUp(-1)
                    self.parent.lheight += 1
                    self.parent.rheight += 1
                    self.lheight -= 2
                    self.parent.left.rheight -= 1
            elif self.rheight-self.lheight > 1:
                if self.right.rheight > self.right.lheight:
                    print("left rotate")
                    self.right.rotateLeft()
                    self.parent.lheight += 1
                    self.rheight -= 2
                    self.parent.adjustHeightUp(-1)
                else:
                    print("double left rotate")
                    self.right.left.rotateRight()
                    self.right.rotateLeft()
                    self.parent.adjustHeightUp(-1)
                    self.parent.lheight += 1
                    self.parent.rheight += 1
                    self.rheight -= 2
                    self.parent.right.lheight -= 1
            
    def find(self,x):
        if self.data == x:
            return self
        elif self.data < x:
            if self.right is None:
                return None
            else:
                return self.right.find(x)
        else:
            if self.left is None:
                return None
            else:
                return self.left.find(x)

    def findPredecessor(self):
        if self.left is None:
            return None
        elif self.left.right is None:
            return self.left
        else:
            pred = self.left.right
            while pred.right is not None:
                pred = pred.right
            return pred
    
    def delete(self,x):
        val = self.find(x)
        if val:
            if val.left is None and val.right is None: # is leaf
                if val.parent:
                    if val == val.parent.left:
                        val.parent.left = None
                    else:
                        val.parent.right = None
                else:
                    val.data = None
            elif val.left and val.right is None: # only left child
                if val.parent is None:
                    val.data = val.left.data
                    val.left = None
                    val.lheight = 0
                elif val == val.parent.left:
                    val.left.parent = val.parent
                    val.parent.lheight -= 1
                    val.parent.left = val.left
                else:
                    val.left.parent = val.parent
                    val.parent.rheight -= 1
                    val.parent.right = val.left
            elif val.right and val.left is None: # only right child
                if val.parent is None:
                    val.data = val.right.data
                    val.left = None
                    val.rheight = 0
                elif val == val.parent.left:
                    val.right.parent = val.parent
                    val.parent.lheight -= 1
                    val.parent.left = val.right
                else:
                    val.right.parent = val.parent
                    val.parent.rheight -= 1
                    val.parent.right = val.right
            else: # has 2 children (is internal node)
                pred = val._findPredecessor() # is not None
                pred.adjustHeightUp(-1)
                self.delete(pred.data)
                val.data = pred.data

        else:
            print (x, "is not in this tree")

    def __iter__(self):
        #BC: Empty
        if self:
            if self.left:
                for x in self.left:
                    yield x
            yield self.data
            if self.right:
                for x in self.right:
                    yield x    


class AVL:
    def __init__(self,val):
        self.tree = AVL_help(val,None,None,None)

    def insert(self,val):
        self.tree.insert(val)
        self.tree = self.tree.root()

    def __contains__(self,x):
        if self.tree.find(x):
            return True
        else:
            return False

    def __delitem__(self,x):
        self.tree.delete(x)

    def inorder(self):
        for x in self.tree:
            print (x, end=" ")
        print()

    def __iter__(self):
        #BC: Empty
        if self.tree:
            if self.tree.left:
                for x in self.tree.left:
                    yield x
            yield self.tree.data
            if self.tree.right:
                for x in self.tree.right:
                    yield x    


# Tests
test = AVL(10)
test.insert(4)
test.insert(20)
test.insert(14)
test.insert(15)
test.insert(16)
test.inorder()
print("14 in test:", 14 in test)
del test[14]
test.inorder()
print("14 in test:", 14 in test)
del test[10]
test.inorder()
