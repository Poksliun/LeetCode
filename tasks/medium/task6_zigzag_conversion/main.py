from urllib.parse import quote


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string_length = len(s)
        if numRows == 1 or numRows == string_length:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        res = ''
        strings_indexes = numRows - 1
        step = strings_indexes * 2
        end = string_length + step
        res += s[0::step]
        for i in range(1, numRows - 1):
            for j in range(i, end, step):
                if 0 < (index := j - i * 2) < string_length:
                    res += s[index]
                if j < string_length:
                    res += s[j]
        res += s[strings_indexes::step]
        return res


sol = Solution()
val = 'ABCDE'

print(sol.convert(val, 4))

# A
# B
# C
# D J
# E

# P0 A1 Y2 P3 A4 L5 I6 S7 H8 I9 R10 I11 N12 G13
# q0 w1 e2 r3 t4 y5 u6 i7 o8 p9 a10 s11 d12 f13 g14 h15 j16 k17 l18


# P    I    N
# A  L S  I G
# Y A  H R
# P    I

# q0     o8     j
# w   i7 p9   h k
# e  u6  a10  g  l
# r y5   s11 f
# t4     d12


# q0    u6    d12   l18
# w1  y5 i7  s11 f13  k17
# e2 t4  o8 a10  g14 j16
# r3    p9    h15

# q   t   o   d   j
# w r y i p s f h k
# e   u   a   g   l
