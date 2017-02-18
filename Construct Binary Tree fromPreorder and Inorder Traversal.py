# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder==[]:
            return []
        node=preorder[0]
        n=inorder.index(node)

        return self.build(node,(preorder[1:n+1],inorder[0:n]),(preorder[n+1:],inorder[n+1:]))
    def build(self,node,left,right):
        #print node,left,right
        a=TreeNode(node)
        if left[0]!=[]:
            nodel=left[0][0]

            n=left[1].index(nodel)
            
            a.left=self.build(nodel,(left[0][1:n+1],left[1][0:n]),(left[0][n+1:],left[1][n+1:]))
        if right[0]!=[]:
            nodel=right[0][0]
            n=right[1].index(nodel)
            a.right=self.build(nodel,(right[0][1:n+1],right[1][0:n]),(right[0][n+1:],right[1][n+1:]))    
            
        return a
        