#Given a linked list, remove the nth node from the end of list and return its head.
#
#For example,
#
#   Given linked list: 1->2->3->4->5, and n = 2.
#
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
#Note:
#Given n will always be valid.
#Try to do this in one pass.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        count = 0
        while current != None: 
            current = current.next
            count += 1 # count the length of the linked list
        
        current = head
        previous = None
        if count - n == 0:
            head = current.next
            
        elif count - n == 1:
            previous = current
            current = current.next
            previous.next = current.next
            
        else:
           for i in range(1, count- n+1):
              previous = current
              current = current.next
           previous.next = current.next
            
        return head
            
