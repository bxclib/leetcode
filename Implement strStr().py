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
        needle_next.append(0)
        needle_next.append(1)

        
        
        for i in range(2,len(needle)):
            j=needle_next[i-1]
            j=j-1        #change to python subscript convention
            while j>=0 and needle[j]!=needle[i-1]:
                j=needle_next[j]
                j=j-1   #change to python subscript convention
        
            if needle[j]==needle[i-1]:
                needle_next.append(j+1+1)     #change to KMP subscript convention
                #print "append1"
            else:
                needle_next.append(1)
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
            if haystack[i]!=needle[j] and j!=-1:   #  0 in KMP convention -1 in python convention
                
                j=needle_next[j]
                j=j-1
                
                
                
                
            else:
                i=i+1
                j=j+1
                #print i,j
        #print "return 2"    
        #return -1
                
        
        
