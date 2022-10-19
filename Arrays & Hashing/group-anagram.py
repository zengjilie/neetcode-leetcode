# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # provide default value for key doesn't exist

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()  # return a list of all the values


# time complexity O(n*m)
# n is the average length of characters in a string, m is the number of strings

# space complexity O(m)

# caveats:
# can't use list as key in python, because key must be immutable, instead use tuple

# summary:
# use defaultdict(value) can create default values for key that doesn't exist