class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[] or nums==[0]:
            return 1
        l=[]
        for i in xrange(max(nums)+1):
            l.append(0)
        for i in nums:
            if i > 0:
                l[i]=i
        #print l
        for i,j in enumerate(l):
            if i!=j:
                return i
        return len(l)
