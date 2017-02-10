class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        l=[]
        square=[]
        self.n=n
        self.putQueens(0,square,l)
        return l
    def notDanger(self,column,square):
        print square,column
        for s,i in enumerate(square):
            
            if i[column]=="Q":
                return False
            
            if column+len(square)-1-s>=0 and column+len(square)-1-s<self.n:
                #print "###"
                #print s,column+len(square)-1-s
                #print len(square)-1,column
                if i[column+len(square)-1-s]=="Q":
                    return False
            if column-len(square)+1+s>=0 and column-len(square)+1+s<self.n:
                if i[column-len(square)+1+s]=="Q":
                    return False
        return True
    def putQueens(self,row,square,l):
        if row==self.n:
            l.append(square)
        else:
            for i in xrange(self.n):
                if (self.notDanger(i,square)):
                    s="."*self.n
                    s=s[:i]+"Q"+s[i+1:]
                    square2=square[::]
                    square2.append(s)
                    #print square2
                    self.putQueens(row+1,square2,l)
    
                
                    
                    
                
            
