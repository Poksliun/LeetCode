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
