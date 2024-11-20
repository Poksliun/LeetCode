class Solution:
    # this decieded is best
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for index, letter in enumerate(haystack):
            if letter == needle[0] and haystack[index: index + needle_len] == needle:
                return index
        return -1


sol = Solution()


def test_1():
    actual = sol.strStr('asadbutsad', 'sad')
    expected = 1
    assert actual == expected


if __name__ == '__main__':
    test_1()
