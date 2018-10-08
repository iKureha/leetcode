# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        
        l3 = ListNode(0)
        pointer = l3
        
        while l1 and l2:
            if l1.val <= l2.val:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next
                
        if l1 == None:
            while l2:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next
        else:
            while l1:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
                
        return l3.next
        
        
        
            
        
