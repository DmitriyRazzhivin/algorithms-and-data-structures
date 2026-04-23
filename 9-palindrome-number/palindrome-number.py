class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversedNumber = 0
        initialNumber = x

        while x > 0:
            lastDigit = x % 10
            reversedNumber = (reversedNumber * 10) + lastDigit
            x = x // 10
       
        return initialNumber == reversedNumber