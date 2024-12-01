class Solution:
    symbol_list = {
        'I': 1,
        'IV': 4,
        'IX': 9,
        'V': 5,
        'X': 10,
        'XL': 40,
        'XC': 90,
        'L': 50,
        'C': 100,
        'CD': 400,
        'CM': 900,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        res: int = 0
        end = len(s)
        i = 0
        while i < end:
            if temp := self.symbol_list.get(s[i:i + 2]):
                res += temp
                i += 2
                continue
            res += self.symbol_list.get(s[i])
            i += 1

        return res

class BestMemorySolution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        total = 0
        i = 0
        while i < len(s):
            if i+1<len(s) and values[s[i]] < values[s[i+1]]:
                total += values[s[i+1]]-values[s[i]]
                i+=1
            else:
                total+=values[s[i]]
            i+=1
        return total


sol = Solution()
# sol = BestMemorySolution()

def test_1():
    assert sol.romanToInt('III') == 3
    return True

def test_2():
    assert sol.romanToInt('LVIII')
    return True

def test_3():
    assert sol.romanToInt('MCMXCIV') == 1994
    return True

def test_4():
    assert sol.romanToInt('IM') == 1001
    return True


if __name__ == '__main__':
    print(test_1())
    print(test_2())
    print(test_3())
    print(test_4())
