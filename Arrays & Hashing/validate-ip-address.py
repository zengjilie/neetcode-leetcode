# https://leetcode.com/problems/validate-ip-address/
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if self.ipv4Check(queryIP):
            return 'IPv4'    
        if self.ipv6Check(queryIP):
            return 'IPv6' 
        return 'Neither'
    
    def ipv4Check(self, queryIP):
        s = queryIP.split('.')
        
        if len(s) != 4:
            return False
        try:
            for x in s:
                if x != str(int(x)) or int(x) not in range(256):
                    return False 
            return True
        except:
            return False
           
    def ipv6Check(self, queryIP):
        s = queryIP.split(':')
        if len(s) != 8:
            return False
        try:
            for x in s:
                if len(x) not in range(1,5) or int(x, 16) < 0:
                    return False
        except:
            return False
        return True

# time complexity O(n)
# space complexity O(1)

# summary
# ipv4: [0 - 2^32]
# ipv6: [0 - 2^128]

# use python error handling to check type casting  