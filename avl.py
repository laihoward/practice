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

class AVL(object):
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            croot = self.find(key)
            if croot.key == key:
                return croot
            New_Node = TreeNode(key, value)
            New_Node.parent = croot    
            if key < croot.key : #左側插入新結點
                croot.left = New_Node
            else:#右側插入新結點
                croot.right = New_Node
            self.rebalance(croot)
            
        # insert and rebalance
    
    def left_rotation(self, croot):
        # TODO: remeber to update parent and take care of root case
        croot_left = croot
        croot = croot.right
        move_node = croot.left
        croot_left.right = move_node
        # croot_left.right = croot.left
        croot.left = croot_left
        croot_left.parent = croot
        if move_node is not None:
            move_node.parent = croot_left 
        return croot

    def right_rotation(self, croot):
        croot_right = croot
        croot = croot.left
        move_node = croot.right
        croot_right.left = move_node
        croot.right = croot_right
        croot_right.parent = croot
        move_node.parent = croot_right
    # TODO: remeber to update parent and take care of root case

    def rebalance(self, croot):
        # TODO: take care of 4 cases of rotation operations
        if self.is_balanced(croot) is True:
            return croot
        else:
            if croot.key < croot.parent.key:
                self.right_rotation(croot.parent) #右旋
                if self.is_balanced(croot) is True:
                    return  #LL-imbalance
                else:
                    self.left_rotation(croot.parent)#左旋
                    return #RL-imbalance
            elif croot.key > croot.parent.key:
                self.left_rotation(croot.parent) #左旋
                if self.is_balanced(croot) is True:
                    return  #RR-imbalance
                else:
                    self.right_rotation(croot.parent)#右旋
                    return  #LR-imbalance

    def is_balanced(self, croot):
        return self.recur_is_balanced(croot)
    # TODO: abs(h_left-h_right) <= 1 

    def recur_is_balanced(self, croot):
        if croot.parent is None:
            return True
        else:
            croot = croot.parent
            if croot.left == None:
                h_left = 0
            else:
                h_left=self.recur_height(croot.left)
            if croot.right == None:
                h_right = 0
            else:
                h_right=self.recur_height(croot.right)
            if abs(h_left-h_right) <= 1:
                return True
            else:
                return False



# l = [5,10,15]
# length = len(l)
# while len(l) > 0:
#     key = l.pop(0)
#     value = chr(key)
#     print(self.in_order())
#     self.insert(key, value)
#     print(self.in_order())
#     # print(tree.is_balanced())
# print(self.in_order())
# print(self.level_order())




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

    def remove(self, key):
        if  self.root is None:
            return 
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
            return 1+max(self.recur_height(croot.left),self.recur_height(croot.right))
    
   
   
# %%
