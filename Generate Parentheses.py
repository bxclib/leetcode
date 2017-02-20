class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result=[]
        self.n=n
        self.putParenthesis(0,"")
        return self.result
    def putParenthesis(self,i,last_str):
        if i==2*self.n:
            self.result.append(last_str)
            return 0
        if last_str.count("(")>last_str.count(")"): 
            last_str2=last_str[::]
            last_str2=last_str2+")"
            self.putParenthesis(i+1,last_str2)
            if last_str.count("(")<self.n:
                last_str1=last_str[::]
                last_str1=last_str1+"("
                self.putParenthesis(i+1,last_str1)
                
        else:
            if last_str.count("(")<self.n:
                last_str1=last_str[::]
                last_str1=last_str1+"("
                self.putParenthesis(i+1,last_str1)
        return 0
