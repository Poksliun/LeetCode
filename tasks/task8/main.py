from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = len(nums) - 1
        while index > 0:
            if nums[index] == val:
                del nums[index]
            index -= 1
        return len(nums)

