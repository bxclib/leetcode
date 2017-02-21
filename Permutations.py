class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[]
        l.append([])
        result=[]
        while l!=[]:
            a=l.pop()
            if len(a)==len(nums):
                result.append(a)
            else:
                for i in nums:
                    if i not in a:
                        a2=a[::]
                        a2.append(i)
                        l.append(a2)
        return result
