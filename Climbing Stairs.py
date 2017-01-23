class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        m2=1
        m1=2
        for i in range(n+1):
            
                m=m1+m2
                m2=m1
                m1=m
                print m
                if i==n-3:
                    
                    return m