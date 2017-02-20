# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.result=[[]]
        self.putNode(root,0)
        return self.result
    def putNode(self,root,i):
        self.result[i].append(root.val)
        
        if root.left is not None:
            if len(self.result)<=i+1:
                self.result.append([])
            self.putNode(root.left,i+1)
        if root.right is not None:
            if len(self.result)<=i+1:
                self.result.append([])
            self.putNode(root.right,i+1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level=[root]
        ans=[]
        while level!=[]:
            temp=[]
            ans.append([])
            for i in level:
                ans[len(ans)-1].append(i.val)
                temp=temp+[i.left,i.right]
            level=[]
            for i in temp:
                if i is not None:
                    level.append(i)
        return ans
                