# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        l=0
        t=head
        while t:
            l+=1
            t=t.next
        target=l-n

        if target==0:
            return head.next
        
        cur=head
        for i in range(l-1):
            if i+1==target:
                cur.next=cur.next.next
                break
            cur=cur.next
        return head



        