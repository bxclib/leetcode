# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        ansmin=ListNode(head.val)
        ansmax=ansmin
        i=head.next
        while i is not None:
            if i.val<ansmin.val:
                temp=ListNode(i.val)
                temp.next=ansmin
                ansmin=temp
                i=i.next
                continue
            if i.val>ansmax.val:
                ansmax=self.insertAfter(ansmax,i.val)
                i=i.next
                continue
            pointer=ansmin
            while pointer.next is not None:
                if pointer.next.val>=i.val:
                    break
                pointer=pointer.next
            self.insertAfter(pointer,i.val)
            i=i.next
        return ansmin
                
            
    def insertAfter(self,node,num):
        n=ListNode(num)
        if node is None:
            return n
        n.next=node.next
        node.next=n
        return n
    
        
            
        
