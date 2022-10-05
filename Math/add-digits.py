# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            while num > 9:
                temp = 0
                while num :
                    temp += num % 10
                    num //= 10 
                num = temp
            return num