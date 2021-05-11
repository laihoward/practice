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
        self.count = []
    
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
        new_croot = croot.right
        croot.right =new_croot.left
        # parent_nodes=croot.parent
        if new_croot.left is not None:
            new_croot.left.parent = croot
        new_croot.parent = croot.parent
        if croot.parent ==None:
            self.root = new_croot
            new_croot.parent = None
        elif croot == croot.parent.left:
            croot.parent.left = new_croot
        else:
            croot.parent.right = new_croot
        new_croot.left = croot
        croot.parent = new_croot
            
    def right_rotation(self, croot):
        new_croot = croot.left
        croot.left =new_croot.right
        if new_croot.right is not None:
            new_croot.right.parent = croot
        new_croot.parent = croot.parent
        if croot.parent ==None:
            self.root = new_croot
        elif croot == croot.parent.right:
            croot.parent.right = new_croot
        else:
            croot.parent.left = new_croot
        new_croot.right = croot
        croot.parent = new_croot
    # TODO: remeber to update parent and take care of root case

    def rebalance(self, croot):
        # TODO: take care of 4 cases of rotation operations
        if self.is_balanced(croot) is True:
            self.count.append('O')
            return croot
        else:
            self.count.append(croot.key)
            croot = self.recur_is_balanced(croot)
            if isinstance(croot, TreeNode):
                self.count.append(croot.key)
                # if croot.key < croot.parent.key:
                if self.recur_height(croot.left)>self.recur_height(croot.right):
                    if self.recur_height(croot.left.left)>self.recur_height(croot.left.right):#LL-imbalance
                        self.right_rotation(croot) #右旋
                        self.count.append('LL')
                    else :#LR-imbalance
                        self.left_rotation(croot.right)#先左旋
                        self.right_rotation(croot)#再右旋
                        self.count.append('LR')
                
                # elif croot.key > croot.parent.key:
                elif self.recur_height(croot.left)<self.recur_height(croot.right):
                    if self.recur_height(croot.right.left)<self.recur_height(croot.right.right):#RR-imbalance
                        self.left_rotation(croot) #左旋
                        self.count.append('RR')
                    else:#RL-imbalance
                        self.right_rotation(croot.left)#先右旋
                        self.left_rotation(croot)#再左旋
                        self.count.append('RL')

    def is_balanced(self, croot):
        if croot.parent is None:
            return True
        else:
            croot = croot.parent
            return self.recur_is_balanced(croot)
    # TODO: abs(h_left-h_right) <= 1 

    def recur_is_balanced(self, croot):
        if croot.left == None:
            h_left = 0
        else:
            h_left=self.recur_height(croot.left)
        if croot.right == None:
            h_right = 0
        else:
            h_right=self.recur_height(croot.right)
        if abs(h_left-h_right) <= 1:
            if self.root.key != croot.key : 
                self.is_balanced(croot.parent)#繼續往croot.parent判斷是否平衡
            else:
                return True #已找到root_node且整棵樹為平衡
        else:
            if abs(h_left)>abs(h_right):
                self.count.append("A")
                return croot#左邊不平衡輸出當下croot.left
            elif abs(h_left)<abs(h_right):
                self.count.append("B")
                # self.count.append(croot.key)
                # self.count.append(croot.right.key)
                # self.count.append(croot.right.right.key)
                return croot#右邊不平衡輸出當下croot.right

            # return croot#不平衡輸出當下croot


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
