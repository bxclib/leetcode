class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ""
        k=0;
        minl=float("inf");
        for j,i in enumerate(strs):
            if len(i)<minl:
                k=j
                minl=len(i)
        res=""
        bool1=True
        for j in xrange(minl):
            a=strs[0][j]
            for i in strs:
                if a!=i[j]:
                    
                   bool1=False 
            if bool1:
                res=res+a
                
            else:
                break
        return res
