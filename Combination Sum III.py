class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result=[]
        self.n=n
        self.k=k
        self.setNum(0,[])
        return self.result
                
                
    def setNum(self,i,list_last):
        sum_last=sum(list_last)
        if list_last==[]:
            maxNum=0
        else:
            maxNum=max(list_last)
        print maxNum
        if i==self.k:
            self.result.append(list_last)
            return 0
        if i==self.k-1: 
            if self.n-sum_last>maxNum and self.n-sum_last<=9 :
                list_last2=list_last[::]
                list_last2.append(self.n-sum_last)
            
            
                self.setNum(i+1,list_last2)
                return 0
            else:
                return 0
        for j in range(1,10):
            
            if j+sum_last<self.n and j>maxNum:
                list_last2=list_last[::]
                list_last2.append(j)
                print j
                self.setNum(i+1,list_last2)

            
        return 0
        
        
