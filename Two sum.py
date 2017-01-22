class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,j in enumerate(nums):
            for h,k in enumerate(nums[i+1:]):
                
                if j+k==target:
                    
                    return [i,h+i+1]