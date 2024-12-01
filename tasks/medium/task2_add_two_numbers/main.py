from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_list = ListNode()
        cur_list = res_list
        while l1 and l2:
            cur_list.val += l1.val + l2.val
            if next_ := cur_list.val // 10:
                cur_list.val %= 10
            if l1.next or l2.next or next_:
                cur_list.next = ListNode(next_)
                cur_list = cur_list.next
            l1, l2 = l1.next, l2.next
        l1 = l1 if l1 else l2
        while l1:
            cur_list.val += l1.val
            if next_ := cur_list.val // 10:
                cur_list.val %= 10
            if l1.next or next_:
                cur_list.next = ListNode(next_)
                cur_list = cur_list.next
            l1 = l1.next

        return res_list



sol = Solution()

def test_1():
    actual = sol.addTwoNumbers(ListNode(9, ListNode(9,ListNode(9))), ListNode(1))
    assert actual == ListNode(1,ListNode(0, ListNode(0, ListNode(0))))

if __name__ == '__main__':
    test_1()