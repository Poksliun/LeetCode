from operator import index


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_, l = 0, ''
        for i in s:
            if i in l:
                if (len_ := len(l)) > max_:
                    max_ = len_
                if l.endswith(i):
                    l = ''
                else:
                    l = l[l.index(i) + 1:]
            l += i
        if (len_ := len(l)) > max_:
            return len_
        return max_


class MyBestSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        full_len = len(s)
        i = full_len
        max_, start = 0, 0
        num_dict = {}
        for i, l in enumerate(s.encode()):
            if num_dict.get(l, -1) >= start:
                if (len_ := i - start) > max_:
                    max_ = len_
                start = num_dict[l] + 1
                if full_len - start < max_:
                    return max_
            num_dict[l] = i
        if (len_ := len(s[start:i + 1])) > max_:
            return len_

        return max_


sol = MyBestSolution()


def test_1():
    act = sol.lengthOfLongestSubstring('abcaabcbb')
    assert act == 1


if __name__ == '__main__':
    test_1()
