class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.append(nums[0])
        self.nums=nums
        self.createHeap(self.nums)
        print self.nums
        res=[]
        while len(res)!=k:
            res.append(self.nums[1])
            self.nums[1],self.nums[len(self.nums)-1]=self.nums[len(self.nums)-1],self.nums[1]
            self.nums.pop()
            self.changeNum(1)
        return res[len(res)-1]
    def createHeap(self,nums):
        k=int(0.5*(len(self.nums)-1))
        while k>0:
            self.changeNum(k)
            k=k-1
            
    def changeNum(self,i):
        if 2*i==len(self.nums)-1:
            if self.nums[i]<self.nums[2*i]:
                self.nums[i],self.nums[2*i]=self.nums[2*i],self.nums[i]
        if 2*i+1<=len(self.nums)-1:
            if self.nums[2*i]>=self.nums[2*i+1]:
                if self.nums[i]<self.nums[2*i]:
                    self.nums[i],self.nums[2*i]=self.nums[2*i],self.nums[i]
                    self.changeNum(2*i)
            else:
                if self.nums[i]<self.nums[2*i+1]:
                    self.nums[i],self.nums[2*i+1]=self.nums[2*i+1],self.nums[i]
                    self.changeNum(2*i+1)
 
        
