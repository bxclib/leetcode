# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxSum(self,root):
        s=0
        s=s+root.val
        a=0
        b=0
        if root.left is not None:
            a=max(self.maxSum(root.left),0)
            s=s+a
    
        if root.right is not None:
            b=max(self.maxSum(root.right),0)
            s=s+b
        if s>self.maxPath:
            self.maxPath=s
            #print s
        return max(a,b)+root.val
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPath=float('-inf')
        self.maxSum(root)
        return self.maxPath