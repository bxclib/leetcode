class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<len(needle):
            return -1

        needle_next=[]
        needle_next.append(-1)
        
        
        for i in xrange(1,len(needle)):
            j=needle_next[i-1]
            while j>=0 and needle[j+1]!=needle[i]:
                j=needle_next[j]
            if needle[j+1]==needle[i]:
                needle_next.append(j+1)
                #print "append1"
            else:
                needle_next.append(-1)
                #print "append2"
        #print needle,needle_next
        l1=len(needle)
        l2=len(haystack)
        i=0
        j=0
        while j<=l1 and i<=l2:
            if j==l1:  
                #print "return 1"
                return i-l1
            if i==l2:
                return -1
            if haystack[i]!=needle[j]:
                
                if j==0:
                    i=i+1
                else:
                    j=needle_next[j-1]+1
                #print "!"
                
            else:
                i=i+1
                j=j+1
                #print i,j
        #print "return 2"    
        #return -1
                
        
        
