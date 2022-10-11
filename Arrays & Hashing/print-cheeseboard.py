# https://leetcode.com/discuss/interview-question/1429515/cisco-oa-2021-masters-internship
def solution(n):
    arr = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                arr[i][j] = 'W'
                print(i, j, 'w')
            else:
                arr[i][j] = 'B'
                print(i, j, 'b')
    return arr

print(solution(2))

# caveat 
# arr = [['']*n]*n will create n duplicated lists
# has to use in range for this problem