from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = len(nums) - 1
        while last > 0:
            count_ = nums.count(nums[last])
            if count_ != 1:
                start = last - count_ + 1
                del nums[start :last]
                last = start
            last -= 1
        return nums


sol = Solution()



def test_1():
    actual = sol.removeDuplicates([1,1,2])
    assert actual == [1,2]

def test_2():
    actual = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    assert actual == [0,1,2,3,4]

if __name__ == '__main__':
    test_1()
    test_2()
