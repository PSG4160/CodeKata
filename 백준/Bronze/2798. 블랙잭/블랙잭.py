from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))

max_sum = 0

for comb in combinations(lst, 3):
    total = sum(comb)
    if total <= M and total >max_sum:
        max_sum = total

print(max_sum)

