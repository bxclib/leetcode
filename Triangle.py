class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==1:
            return triangle[0][0]
        i=len(triangle)-2
        dp=triangle[i]
        
        while i>=0:
            for j,k in enumerate(triangle[i]):
               #print i,j
               triangle[i][j]=triangle[i][j]+min(triangle[i+1][j],triangle[i+1][j+1]) 
            i=i-1
        return triangle[0][0]
        
