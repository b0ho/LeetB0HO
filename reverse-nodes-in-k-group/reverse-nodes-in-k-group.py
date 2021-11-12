# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        init = head
        before = None
        now = head
        after = None
        
        for i in range(k):
            if init is None:
                return head
            else:
                init = init.next
        
        for i in range(k):
            after = now.next
            now.next = before
            before = now 
            now = after
        
        head.next = self.reverseKGroup(now, k)
        
        return before
    
        