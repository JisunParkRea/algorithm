import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
com_num = combinations([int(i) for i in sys.stdin.readline().split()], 3)
max_sum = 0
for nums in com_num:
    s = sum(nums)
    if s==m:
        max_sum = m
        break
    if s<m and s>max_sum:
        max_sum = s
print(max_sum)