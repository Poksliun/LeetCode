class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        cur = first
        while cur.next:
            if first.val != cur.next.val:
                first.next = cur.next
                first = cur.next
            cur = cur.next
        if first.val == cur.val:
            first.next = None
        return head
