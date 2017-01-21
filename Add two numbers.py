# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import *
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        solu=ListNode(0)
        l=[]
        l.append(solu)
        i=0
        while True:
            
            sum=l1.val+l2.val+l[i].val
            l[i].val=(sum)%10
            l[i].next=ListNode((sum)/10)
            l.append(l[i].next)
            #print "i",i
            #print "l[i].val",l[i].val
            #print "l[i].next.val",l[i].next.val
            l1=l1.next
            l2=l2.next
            if l1 is None:
                l1=ListNode(0)
            if l2 is None:
                l2=ListNode(0)
            
            if l1.val+l2.val+l[i].next.val==0 and l1.next is None and l2.next is None:
                l[i].next=None
                break
            i=i+1
        #print l[0].val
        #print l[1].val
        #print l[2].val
        #print l[3].val
        #print (id(l[0]))
        #print (id(l[0].next))
        #print (id(l[1]))
        #print (id(l[1].next))
        #print (id(l[2]))
        
        return l[0]
    
        