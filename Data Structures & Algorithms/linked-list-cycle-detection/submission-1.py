# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=slow=head
        while fast:
            if fast.next == None or fast.next.next == None:
                return False

            fast=fast.next.next
            slow=slow.next
            if fast and slow and fast.val == slow.val:
                return True
        return False
        