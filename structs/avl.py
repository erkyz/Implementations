# An AVL tree for objects with ordering (__lt__)

# AVL tree helper - no interfaces in Python?
class AVL_help:
    def __init__(self,key,left,right,parent):
        # B.C. none for all
        self.left = left
        self.right = right
        self.parent = parent # this is a pointer, right??
        self.key = key
        self.lheight = 0
        self.rheight = 0

    def rotateLeft(self):
        # REQUIRE self.parent is not None, self.parent.right == self
        self.parent.right = self.left
        if self.parent.right:
            self.parent.right.parent = self.parent
        self.left = self.parent
        if self.left.parent:
            if self.left.parent.left.key == self.left.key:
                self.left.parent.left = self
            else:
                self.left.parent.right = self
        self.parent = self.left.parent
        self.left.parent = self 

    def rotateRight(self):
        # REQUIRE self.parent is not None, self.parent.left == self
        self.parent.left = self.right
        if self.parent.left:
            self.parent.left.parent = self.parent
        self.right = self.parent
        if self.right.parent:
            if self.right.parent.left and self.right.parent.left.key == self.right.key:
                self.right.parent.left = self
            else:
                self.right.parent.right = self
        self.parent = self.right.parent
        self.right.parent = self

    def adjustHeightUp(self,dh):
        if self.parent is not None:
            if self.parent.left and self.parent.left.key == self.key:
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
   
    def rebalance(self):
        # could do "pattern match" rebalancing, use "balance factor"
        if self.lheight-self.rheight > 1:
            if self.left.lheight > self.left.rheight:
                self.left.rotateRight()
                self.parent.rheight += 1
                self.lheight -= 2
                self.parent.adjustHeightUp(-1)
            else:
                self.left.right.rotateLeft()
                self.left.rotateRight()
                self.parent.adjustHeightUp(-1)
                self.parent.lheight += 1
                self.parent.rheight += 1
                self.lheight -= 2
                self.parent.left.rheight -= 1
        elif self.rheight-self.lheight > 1:
            if self.right.rheight > self.right.lheight:
                self.right.rotateLeft()
                self.parent.lheight += 1
                self.rheight -= 2
                self.parent.adjustHeightUp(-1)
            else:
                self.right.left.rotateRight()
                self.right.rotateLeft()
                self.parent.adjustHeightUp(-1)
                self.parent.lheight += 1
                self.parent.rheight += 1
                self.rheight -= 2
                self.parent.right.lheight -= 1


    def insert(self,x):
        if self.key is None:
            self.key = x
        else:
            if x >= self.key:
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
            
            # invariant of abs(lheight-rheight) <= 1 may be broken here
            self.rebalance()

    def find(self,x):
        if self.key is None:
            return None
        elif self.key == x:
            return self
        elif self.key < x:
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
    
    def delete(self,key):
        rem = self.find(key)
        if rem:
            if rem.left is None and rem.right is None: # is leaf
                if rem.parent:
                    if rem.parent.left and rem.key == rem.parent.left.key:
                        rem.parent.left = None
                    else:
                        rem.parent.right = None
                else:
                    rem.key = None
            elif rem.left and rem.right is None: # only left child
                if rem.parent is None:
                    rem.key = rem.left.key
                    rem.left = None
                    rem.lheight = 0
                elif rem.parent.left and rem.key == rem.parent.left.key:
                    rem.left.parent = rem.parent
                    rem.adjustHeightUp(-1)
                    rem.parent.left = rem.left
                else:
                    rem.left.parent = rem.parent
                    rem.adjustHeightUp(-1)
                    rem.parent.right = rem.left
            elif rem.right and rem.left is None: # only right child
                if rem.parent is None:
                    rem.key = rem.right.key
                    rem.left = None
                    rem.rheight = 0
                elif rem.parent.left and rem.key == rem.parent.left.key:
                    rem.right.parent = rem.parent
                    rem.adjustHeightUp(-1)
                    rem.parent.left = rem.right
                else:
                    rem.right.parent = rem.parent
                    rem.adjustHeightUp(-1)
                    rem.parent.right = rem.right
            else: # has 2 children (is internal node)
                pred = rem.findPredecessor() # is not None
                self.delete(pred.key)
                rem.key = pred.key

        else:
            print (key, "is not in this tree")

    def __iter__(self):
        #BC: Empty
        if self:
            if self.left:
                for x in self.left:
                    yield x
            yield self.key
            if self.right:
                for x in self.right:
                    yield x    


class AVL:
    def __init__(self,keys):
        self.tree = AVL_help(None,None,None,None)
        for key in keys:
            self.insert(key)

    def insert(self,key):
        self.tree.insert(key)
        self.tree = self.tree.root()

    def find(self,key):
        return self.tree.find(key) is not None

    def __contains__(self,x):
        return self.find(x)

    def __delitem__(self,x):
        self.tree.delete(x)

    def __iter__(self):
        if self.tree.key:
            if self.tree.left:
                for x in self.tree.left:
                    yield x
            yield self.tree.key
            if self.tree.right:
                for x in self.tree.right:
                    yield x    



# Python implements dictionaries as hash tables. I'm going to use an AVL tree, obviously less efficient

class AVL_dict_help(AVL_help):
    def __init__(self,key,val,left,right,parent):
        # B.C. none for all
        self.left = left
        self.right = right
        self.parent = parent # this is a pointer, right??
        self.key = key
        self.val = val
        self.lheight = 0
        self.rheight = 0

    def insert(self,key,val):
        if self.key is None:
            self.key = key
            self.val = val
        else:
            if key >= self.key:
                if self.right is None:
                    self.right = AVL_dict_help(key,val,None,None,self)
                    self.rheight = 1
                    if self.left is None:
                        self.adjustHeightUp(1)
                else:
                    self.right.insert(key,val)
            else:
                if self.left is None:
                    self.left = AVL_dict_help(key,val,None,None,self)
                    self.lheight = 1
                    if self.right is None:
                        self.adjustHeightUp(1)
                else:
                    self.left.insert(key,val)
       
        self.rebalance()


class AVL_dict(AVL):
    def __init__(self,items):
        self.tree = AVL_dict_help(None,None,None,None,None)
        for item in items:
            self.insert(item,items[item])

    def insert(self,key,val):
        self.tree.insert(key,val)
        self.tree = self.tree.root()

    def __setitem__(self,key,val):
        self.insert(key,val)

    def __getitem__(self,key):
        res = self.tree.find(key)
        if res:
            return res.val
        return res

    # TODO setdefault, values()
