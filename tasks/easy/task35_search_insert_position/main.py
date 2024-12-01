from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        right = len(nums) - 1
        left = 0
        if target <= nums[left]:
            return 0
        if target > nums[right]:
            return right + 1
        middle = (left + right) // 2
        while left != right:
            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle
            middle = (left + right) // 2
        return middle




class BestSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return r + 1

sol = Solution()
array_ = [1,3,4,5,6]

def test_1():
    actual = sol.searchInsert(array_, 5)
    assert actual == 3

def test_2():
    actual = sol.searchInsert(array_, 2)
    assert actual == 1

def test_3():
    actual = sol.searchInsert(array_, 7)
    assert actual == 5

def test_4():
    actual = sol.searchInsert([1,3], 2)
    assert actual == 1

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
