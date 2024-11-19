from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not(list1 and list2):
            return None
        list3 = ListNode()
        cp = list3
        while list1 and list2:
            list1, list2 = (list1, list2) if list1.val <= list2.val else (list2, list1)
            cp.val = list1.val
            list1 = list1.next
            if list1 and list2:
                cp.next = ListNode()
                cp = cp.next
        while list2:
            cp.next = ListNode(list2.val)
            list2 = list2.next
            if list2:
                cp = cp.next

        return list3







sol = Solution()


def test_1():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    res = sol.mergeTwoLists(list1, list2)
    assert res == list3
    return True


if __name__ == '__main__':
    print(test_1())
