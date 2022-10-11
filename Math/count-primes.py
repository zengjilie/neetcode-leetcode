# https://leetcode.com/problems/count-primes/

# Naive approach
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0

        prime = [1] * n
        prime[0] = prime[1] = 0

        for i in range(2, n):
            if prime[i] == 1:
                for multiple in range(i*i, n, i):
                    prime[multiple] = 0

        return sum(prime)
