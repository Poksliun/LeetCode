class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        max_len = 0
        res = ''
        for i in range(len_s):
            if len_s - i <= max_len:
                break
            for j in range(len_s, i, -1):
                if j - i <= max_len:
                    break
                string_ = s[i:j]
                if string_ == string_[::-1] and len(string_) > max_len:
                    max_len = len(s[i:j])
                    res = string_
        return res

