# %%
import math
class TreeNode(object):
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    
    # def __del__(self):
    #     print(f'TreeNode with data {self.key} is destroyed')

class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            croot = self.find(key)
            if croot.key == key:
                return croot
            elif croot.key != key:
                New_Node = TreeNode(key, value)
                New_Node.parent = croot
                if key < croot.key :
                    croot.left = New_Node
                elif key > croot.key:
                    croot.right = New_Node
                return croot
            # TODO: if croot.key == key, then we should stop insert operation.
            # if croot.key != key, croot would be the parent of new node.
    def find(self, key):
        return self.recur_find(self.root, key)
    
    def recur_find(self, croot, key):
        if croot.key == key:
            return croot
        else:
            if croot.left is None and croot.right is None:
                return croot
            else:
                if key < croot.key :
                    if croot.left != None:
                        return self.recur_find(croot.left,key)
                    else:
                        return croot
                elif key > croot.key:
                    if croot.right != None:
                        return self.recur_find(croot.right,key)
                    else:
                        return croot
        # TODO: As you can see, insert and find operations are very similar.
        # We should modify find operation. 
        # If key is not found, we should return a node which is suitable to be 
        # the parent of the new node.
        # Example:
        #         38
        #      13    51
        # find(50), should return 51

    # def remove(self, key):
    #     # TODO: Now we store parent pointer, 
    #     # Please remember to update the parent after remove.
    
    # def two_child_remove(self, croot):

    # def zero_one_child_remove(self, croot):

    # def right_most_child(self, croot):


    def pre_order(self):
        res = list()
        return self.recur_pre_order(self.root, res)
    
    def recur_pre_order(self, croot, res):
        if croot is None:
            return
        else:
            res.append(croot.key)
            self.recur_pre_order(croot.left, res)
            self.recur_pre_order(croot.right, res)
        return res

    def in_order(self):
        res = list()
        return self.recur_in_order(self.root, res)
    
    def recur_in_order(self, croot, res):
        if croot is None:
            return
        else:
            self.recur_in_order(croot.left, res)
            res.append(croot.key)
            self.recur_in_order(croot.right, res)
        return res

    # def level_order(self):
    
    # def height(self):

    # def recur_height(self, croot):
        
    # def mirror(self):
        
    # def recur_mirror(self, croot):
    
    # def print_paths(self):
        
    # def recur_print_paths(self, croot, s, l):
# %%
