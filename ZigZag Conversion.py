class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s=="" or numRows==1:
            return s
        
        l=[]
        for i in range(numRows):
            l.append("")
        p=0
        column=len(s)
        #print column
        for i in range(column):
            for j in range(numRows):
                tmp=i%(numRows-1)
                if tmp==0:
                    l[j]=l[j]+s[p]
                    #print s[p]
                    #print i,j
                    p=p+1
                    #print "append much"
                else:
                    j=(numRows-1)-tmp
                    l[j]=l[j]+s[p]
                    #print s[p]
                    #print i,j
                    p=p+1
                    break
                if p==len(s):
                    break
            if p==len(s):
                    break
        #print l
        s1=""
        for i in l:
            #print i
            s1=s1+i
        

        return s1