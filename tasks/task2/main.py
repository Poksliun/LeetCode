class MySolution:
    def isPalindrome(self, x: int) -> bool:
        # I checkout boundary values and other keys
        if x == 0:
            return True
        if x < 0:
            return False
        elif not x % 10:
            return False

class BestSolution
    def isPalindrome(self, x: int) -> bool:
        check = str(x)
        left, right = 0, len(check)-1
        while left < right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1
        return True



if __name__ == '__main__':
    number = int(input("Text your number: \n>>> "))
    print(MySolution().isPalindrome(number))
