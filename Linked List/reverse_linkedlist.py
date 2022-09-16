# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev

# time complexity O(n) 
# space complexity O(1)

# caveats
# make None value Node is important mind-set 