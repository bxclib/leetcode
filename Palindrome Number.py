class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x<0:
            return False
        i=0;
        while x>=10**i:
            i=i+1
        #print i
        
        
        i=i-1
        while True:
            a=int(10**i)
            #print "a",a
            #print "x",x
            if x/a!=x%10:
                return False
            x=x-(x/a)*a
            x=x/10
            #print "x",x
            i=i-2
            #print "i",i
            if i<0:
                break
        return True
