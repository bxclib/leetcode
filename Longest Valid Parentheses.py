class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        maxlength=0
        
        for i,k in enumerate(s):
            if k=="(":
                l.append((i,k))
                
            else:
                if l==[]:
                    l.append((i,k))
                elif l[len(l)-1][1]=='(':
                    l.pop()
                    if l==[]:
                        length=i+1
                    else:
                        length=i-l[len(l)-1][0]
                    
                    maxlength=max(maxlength,length)
                else:
                    l.append((i,k))
                    
        return maxlength
