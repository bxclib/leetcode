class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pricem=prices[::]
        for i in range(1,len(pricem)-1):
            pricem[len(pricem)-1-i]=max(pricem[len(pricem)-1-i],pricem[len(pricem)-i])
        m=[]
        for i in range(len(pricem)-1):
            m.append(pricem[i+1]-prices[i])
        m.append(0)
        return max(m)
        
