class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ly=len(grid)
        lx=len(grid[0])
        sum=0
        for i in xrange(ly):
            for j in xrange(lx):
                sum=sum+self.water(i,j,lx,ly,grid)
                
        return sum        
    def water(self,i,j,lx,ly,grid):
        if grid[i][j]==0:
            return 0
        sum=0
        if i==0:
            sum=sum+1
        elif grid[i-1][j]==0:
            sum=sum+1
        if j==0:
            sum=sum+1
        elif grid[i][j-1]==0:
            sum=sum+1
        if j==lx-1:
            sum=sum+1
        elif grid[i][j+1]==0:
            sum=sum+1
        if i==ly-1:
            sum=sum+1
        elif grid[i+1][j]==0:
            sum=sum+1
        #print sum
        return sum