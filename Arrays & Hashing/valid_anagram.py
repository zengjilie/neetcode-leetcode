# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # method 1
        # convert str to char list, and compare them using a for loop
        if len(s) != len(t):
            return False

        list1 = []
        list2 = []
        for char in s:
            list1.append(char)
        for char in t:
            list2.append(char)

        list1.sort()
        list2.sort()

        return list1 == list2
