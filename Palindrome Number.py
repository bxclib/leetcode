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
        a=1;
        while x>=a:
            a=a*10
            i=i+1
        #print i
        
        
        i=i-1
        a=int(10**i)
        while True:
            
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
            a=a/100
        return True
