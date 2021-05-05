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

    def remove(self, key):
        # TODO: Now we store parent pointer, 
        # Please remember to update the parent after remove.
        if  self.root is None:
            return 
        # croot = self.find(key)
        croot = self.root
        while key != croot.key:
            if key > croot.key:
                if croot.right is not None:
                    croot = croot.right
                else:
                    croot = None
                    break
            elif key < croot.key:
                if croot.left is not None:
                    croot = croot.left
                else:
                    croot = None
                    break
            
        if  croot is None:
            return 
        if croot.left is not None and croot.right is not None:
            self.two_child_remove(croot)
        else:
            self.zero_one_child_remove(croot)
    
    def two_child_remove(self, croot):
        iop = self.right_most_child(croot.left)
        croot.key = iop.key
        croot.value = iop.value
        self.zero_one_child_remove(iop)


    def zero_one_child_remove(self, croot):
        parent = croot.parent
        if parent.left is not None and parent.left.key == croot.key:
            if croot.left  is not None:
                parent.left = croot.left
                croot = croot.left
                croot.parent = parent
            elif croot.right  is not None:
                parent.left = croot.right
                croot = croot.right
                croot.parent = parent
            else :
                parent.left =None
            
            
        elif parent.right is not None and parent.right.key == croot.key:
            if croot.left  is not None:
                parent.right = croot.left
                croot = croot.left
                croot.parent = parent
            elif croot.right  is not None:
                parent.right = croot.right
                croot = croot.right
                croot.parent = parent
            else :
                parent.right = None
            
            


    def right_most_child(self, croot):
        if croot.right != None:
            return  self.right_most_child(croot.right)
        else:
            return croot


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

    def level_order(self):
        queue = [self.root]
        res = list()
        while len( queue) > 0:       
            cur = queue[0]
            res.append(cur.key)
            queue = queue[1:]
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
        return res
    
    def height(self):
        if self.root != None:
            return self.recur_height(self.root)
        else:
            return -1

    def recur_height(self, croot):
        if croot ==None:
            return 0
        else:
            return max(self.recur_height(croot.left),self.recur_height(croot.right))
    def mirror(self):
        if self.root is None: 
            return
        self.recur_mirror(self.root)

    def recur_mirror(self, croot):
        if croot != None:
            left_node = croot.left 
            croot.left = croot.right
            croot.right = left_node
            self.recur_mirror(croot.left)
            self.recur_mirror(croot.right)
            return croot
    
    def print_paths(self):
        if self.root is None: 
            return
        s = ''
        l = list()
        self.recur_print_paths(self.root, s,l)
        return l
        
    def recur_print_paths(self,croot, s,l):
        s=f'{s} {croot.key}'
        if  croot.left == None and croot.right == None:
            l.append(s)
        if  croot.left != None:
            self.recur_print_paths(croot.left,s,l)
        if  croot.right != None:  
            self.recur_print_paths(croot.right,s,l)
# %%
