import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=1
        while True:
            s=0.5*(s+x*1.0/s)
            if abs(s**2-x)<0.001:
                break
        print s
        return int(math.floor(s))