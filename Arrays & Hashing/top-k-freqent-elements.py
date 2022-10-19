# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for n, c in hashmap.items():
            count[c].append(n)

        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

# time complexity O(n)
# space complexity O(n)

# hashmap part is the same 
# create a list use index -> freqency,
#  0, 1,  2,  3, 4, 5
#[[],[3],[2],[1],[],[]]
# pointer move reverse direction
