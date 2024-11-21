

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        short, long = sorted((list(a), list(b)), key=len)
        for i in range(-1, -(len(short) + 1), -1):
            if short[i] == '0':
                continue
            j = i
            while j != -(len(long) + 1) and long[j] != '0' :
                long[j] = '0'
                j -= 1
            if j == -(len(long) + 1):
                long.insert(j + 1, '1')
                continue
            long[j] = '1'
        return ''.join(long)


class BestSolution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)

        sum_int = a_int + b_int

        return bin(sum_int)[2:]

        # return '{0:b}'.format(sum_int)



sol = Solution()
# sol = BestSolution()


def test_1():
    actual = sol.addBinary('11', '1')
    assert actual == '100'

def test_2():
    actual = sol.addBinary('1010', '1011')
    assert actual == '10101'

def test_3():
    actual = sol.addBinary('1010', '1011')
    assert actual == '10101'

if __name__ == '__main__':
    test_1()
    test_2()






