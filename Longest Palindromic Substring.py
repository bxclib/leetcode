class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        if len(s)==2:
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        dp=[[False for i in xrange(len(s))] for i in xrange(len(s))]
        #print dp
        for i in xrange(len(s)):
            dp[i][i]=True
        #print dp
        a=0
        b=1
        for i in xrange(len(s)):
            if i<len(s)-1:
                if s[i]==s[i+1]:
                    dp[i][i+1]=True
                    a=i
                    b=i+2
        for i in xrange(3,len(s)+1):
            for j in xrange(i,len(s)+1):
                #print j-i,j-1
                if s[j-i]==s[j-1]:
                    
                    if dp[j-i+1][j-2] is True:
                        dp[j-i][j-1]=True
                        a=j-i
                        b=j
                
        return s[a:b]

        
        
        
                        
                    
    
        
