class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(abs(x))
        
        a=0
        for i,k in enumerate(s):
            a=a+int(k)*10**int(i)
            if a>=2**31:
                return 0
        
        if x>=0:
            return a
        else:
            return -a
