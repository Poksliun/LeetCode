class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        before = 1
        now = 2
        for i in range(n - 2):
            before, now = now, before + now
        return now



sol = Solution()

def test_1():
    actual = sol.climbStairs(2)
    assert actual == 2

def test_2():
    actual = sol.climbStairs(3)
    assert actual == 3

def test_3():
    actual = sol.climbStairs(4)
    assert actual == 5

def test_4():
    actual = sol.climbStairs(5)
    assert actual == 8

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()