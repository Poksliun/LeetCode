class Solution:

    def reverse(self, x: int) -> int:
        seq = 1
        if x < 0:
            seq = -1
            x *= -1
        deg = 1
        answ = 0
        while x != 0:
            answ *= 10
            answ += x % 10
            x //= 10 ** deg

        if len(bin(answ)) - 2 >= 32:
            return 0
        return answ * seq

