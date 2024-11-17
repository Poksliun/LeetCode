from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i, letter in enumerate(strs[0]):
            eq_count = 0
            for word in strs[1:]:
                if i < len(word)  and letter == word[i]:
                    eq_count += 1
                else:
                    break
            else:
                res += letter
                continue
            break

                
        return res

class BestSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        ans=""
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                return ans
        return ans


# sol = Solution()
sol = BestSolution()

def test_1():
    assert sol.longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    return True


def test_2():
    assert sol.longestCommonPrefix(['dog', 'rececar', 'car']) == ''
    return True

def test_3():
    assert sol.longestCommonPrefix(['ab', 'a']) == 'a'
    return True

if __name__ == '__main__':
    print(test_1())
    print(test_2())
    print(test_3())
