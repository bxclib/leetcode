class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        r=[[1]]
        for i in range(numRows-1):
            row=[]
            for j in range(len(r[i])-1):
                row.append(r[i][j]+r[i][j+1])
            row=[1]+row
            row=row+[1]
            r.append(row)

        return r
