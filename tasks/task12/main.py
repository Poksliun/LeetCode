from typing import List

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        last: int = len(digits) - 1
        digits[last] = (digits[last] + 1) % 10
        if digits[last] != 0:
            return digits
        if last == 0:
            digits.insert(0, 0)
            last += 1
        digits[:last] = self.plusOne(digits[:last])
        return digits


sol = Solution()


def test_1():
    actual = sol.plusOne([1,2,3])
    assert actual == [1,2,4]


def test_2():
    actual = sol.plusOne([4,3,2,1])
    assert actual == [4,3,2,2]

def test_3():
    actual = sol.plusOne([9])
    assert actual == [1,0]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
