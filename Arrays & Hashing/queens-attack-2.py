# https://www.hackerrank.com/challenges/queens-attack-2/problem

def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]
    s = set()
    for r, c in obstacles:
        s.add((r, c))

    res = 0
    for r, c in directions:
        row = r_q+r
        col = c_q+c
        while (row in range(1, n+1) and
                col in range(1, n+1) and
                (row, col) not in s):
            res += 1
            row += r
            col += c
    return res

# time complexity O(n^2)
# space complexity O(1)

# summary use hashset to get better time complexity for fast checking
