# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        l=[]
        l.append(root)
        result=[]
        while l!=[]:
            a=l.pop()

                
            if a.right is not None:
                l.append(a.right)
            if a.left is None:
                result.append(a.val)
            else:
                l.append(TreeNode(a.val))
                l.append(a.left)


        return result