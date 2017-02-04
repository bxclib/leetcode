class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                l.append(i)
            elif i==")":
                if l==[]:
                    return False
                elif l[len(l)-1]=="(":
                    l.pop()
                else:
                    return False
            elif i=="]":
                if l==[]:
                    return False
                elif l[len(l)-1]=="[":
                    l.pop()
                else:
                    return False
            elif i=="}":
                if l==[]:
                    return False
                elif l[len(l)-1]=="{":
                    l.pop()
                else:
                    return False
        if l==[]:
            return True
        return False
