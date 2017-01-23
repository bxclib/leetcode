class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry=1
        for k,i in enumerate(digits[::-1]):
            tmp=i+carry
            digits[k]=tmp%10
            carry=tmp/10
        #print digits
        
        if carry!=0:
            '''if len(digits)>3:
                while True:
                    pass'''
            digits.append(carry)
            digits.reverse()
            return digits
        else:
            return digits[::-1]
