S = int(input())
lst = list(map(int, input().split()))

sum_list = sum(lst)
max_score = max(lst)

new_average = (sum_list * 100) / (max_score * S )

print(new_average)
