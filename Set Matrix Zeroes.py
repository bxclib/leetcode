class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row=1
        col=1
        for i in matrix[0]:
            if i==0:
                row=0
                break
        for j in range(len(matrix)):
            if matrix[j][0]==0:
                #print matrix[j][0]
                col=0
                break
        
        for i in range(1,len(matrix[0])):
            tmp=1
            for j in range(1,len(matrix)):
                tmp=tmp*matrix[j][i]
                if tmp==0:
                    matrix[0][i]=0
                    break
        for j in range(1,len(matrix)):
            tmp=1
            for i in range(1,len(matrix[0])):
                tmp=tmp*matrix[j][i]
                if tmp==0:
                    matrix[j][0]=0
                    break
        #print matrix,col,row
        for i in range(1,len(matrix[0])):
            for j in range(1,len(matrix)):
                if matrix[j][0]==0 or matrix[0][i]==0:
                    #print i,j
                    matrix[j][i]=0
        
        if row==0:
            matrix[0]=[0]*len(matrix[0])
            #print "row"
         
        if col==0:
            for j in range(len(matrix)):
                matrix[j][0]=0
                #print "col"
