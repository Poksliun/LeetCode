class Solution:

    def myAtoi(self, s: str) -> int:
        max_ = 2147483647
        min_ = -2147483648
        s: str = s.strip()
        numb: str = ''
        sign = 1
        if len(s) == 0:
            return 0
        elif not s[0].isdigit() and s[0] not in ('+', '-'):
            return 0
        elif not s[0].isdigit():
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        for char in s:
            if char.isdigit():
                numb += char
            else:
                break
        res: int = int(numb) * sign if numb else 0
        return min(max(res, min_), max_)


sol = Solution()


def test_1():
    assert sol.myAtoi('   -042') == -42
    return True


if __name__ == '__main__':
    print(test_1())
