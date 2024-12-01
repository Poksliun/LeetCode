class Solution:
    def mySqrt(self, x: int) -> int:
        appr = x
        while appr * appr > x:
            appr //= 2
        while appr * appr < x and ((appr + 1) * (appr + 1) <= x):
            if appr * appr > x:
                appr = appr // 2
            else:
                appr += 1
        return appr

class GeronSolution:
    def mySqrt(self, x: int) -> int:
        appr = x
        while appr * appr > x:
            appr = 0.5 * (appr + x / appr)
        return int(appr)

class BestSolution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low+high)//2
            sq = mid*mid
            if sq == x :
                return mid
            elif sq < x:
                low = mid+1
            else:
                high = mid -1
        return high


sol = Solution()

def test_1():
    actual = sol.mySqrt(4)
    assert actual == 2

def test_2():
    actual = sol.mySqrt(8)
    assert actual == 2

def test_3():
    actual = sol.mySqrt(6)
    assert actual == 2

def test_4():
    actual = sol.mySqrt(9)
    assert actual == 3

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
