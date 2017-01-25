class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a=height[0]
        b=height[len(height)-1]
        ai=0
        bi=len(height)-1
        s=min(a,b)*(bi-ai)
        
        while ai<bi-1:
            if a<=b:
               ai=ai+1
               a=height[ai]
               s=max(s,min(a,b)*(bi-ai))
            elif a>b:
               bi=bi-1
               b=height[bi]
               s=max(s,min(a,b)*(bi-ai))
            
            
            
        return s