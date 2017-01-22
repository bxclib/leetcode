class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
    
        """
        last="1"
        s=""
        for i in range(n):
            print i
            s=str(last)
            
            last=self.next(last)
        return s
    def next(self,last):
        i_last=last[0]
        j=0
        s=""
        for i in last:
            if i==i_last:
                j=j+1
            else:
                s=s+str(j+1)+i_last
                j=0
            i_last=i
        s=s+str(j+1)+i_last
        s1=str(int(s[0])-1)+s[1:]
        return s1
