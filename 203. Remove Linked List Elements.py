# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        previous = None
        while current != None:
            if current.val == val:
                if current == head:
                    head = current.next
                    current = head
                    continue
                else:
                    
                    previous.next = current.next
                    current = current.next
                    continue
            previous = current
            current = current.next
        
        return head
