# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from copy import * 
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return None
        head=TreeNode(nums[0])
        head.height=0
        for i in nums[1:]:
            self.putNode(head,i)
        return head
    def height(self,node):
        a=-1 if (node.left is None) else node.left.height
        b=-1 if (node.right is None) else node.right.height
        return max(a,b)+1
    def balance(self,node):
        a=-1 if (node.left is None) else node.left.height
        b=-1 if (node.right is None) else node.right.height
        return a-b
    def putNode(self,node,num):
        #print "node",node.val
        #print "num",num
        if node.val==num:
            return None
        if node.val>num:
            if node.left is None:
                node.left=TreeNode(num)
                node.left.height=0
                node.height=self.height(node)
                node.balance=self.balance(node)
                return node.height
            else:
                self.putNode(node.left,num)
                node.height=self.height(node)
                node.balance=self.balance(node)
                #print node.val,node.balance,"nodebalance",node.height
                if 2==node.balance:
                    if node.left.balance==1:
                        #print "LL"
                        self.SingRotateLeft(node)
                    else:
                        #print "LR"
                        self.DoubleRotateLeft(node)
                return node.height
        if node.val<num:
            if node.right is None:
                node.right=TreeNode(num)
                node.right.height=0
                node.height=self.height(node)
                node.balance=self.balance(node)
                return node.height
            else:
                self.putNode(node.right,num)
                node.height=self.height(node)
                node.balance=self.balance(node)
                #print node.val,node.balance,"nodebalance",node.height
                if -2==node.balance:
                    if node.right.balance==-1:
                        #print "RR"
                        self.SingRotateRight(node)
                    else:
                        #print "RL"
                        self.DoubleRotateRight(node)
                return node.height
    def SingRotateLeft(self,node):
        node2=copy(node)
        node2.left=node.left.right
        node.val=node.left.val
        node.left=node.left.left
        node.right=node2
        node.right.height=self.height(node.right)
        node.height=self.height(node)
    def SingRotateRight(self,node):
        node2=copy(node)
        node2.right=node.right.left
        node.val=node.right.val
        node.right=node.right.right
        node.left=node2
        node.left.height=self.height(node.left)
        node.height=self.height(node)
    def DoubleRotateLeft(self,node):
        self.SingRotateRight(node.left)
        self.SingRotateLeft(node)
    def DoubleRotateRight(self,node):
        self.SingRotateLeft(node.right)
        self.SingRotateRight(node)
       
        
        
        
