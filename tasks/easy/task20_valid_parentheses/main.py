from collections import deque

class Solution:
    dct = {'(': ')', '{': '}', '[': ']'}

    def isValid(self, s: str) -> bool:
        opened = ['']
        for i in s:
            if i == self.dct.get(opened[-1]):
                opened.pop()
            else:
                opened.append(i)
        if len(opened) > 1:
            return False
        return True

sol = Solution()

def test_1():
    assert sol.isValid('()')
    return True

def test_2():
    assert not sol.isValid('(]')
    return True

def test_3():
    assert sol.isValid('([])')
    return True

if __name__ == '__main__':
    print(test_1())
    print(test_2())
    print(test_3())

