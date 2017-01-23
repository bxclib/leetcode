class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            return 1.0/self.pow(x,-n)
        elif n==0:
            if x!=0:
                return 1
            else:
                raise Exception('0^0!')
        else:
            return self.pow(x,n)
    
    def pow(self, x, n):
        if n!=0 and n!=1:
            if n%2==0:
                return self.pow(x*x,n/2)
            else:  
                return self.pow(x*x,n/2)*x
        elif n==0:
            return 1
        else:
            return x