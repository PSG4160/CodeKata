import math

N = int(input())
lst = list(map(int, input().split()))

answer = 0

for i in lst:
    if i < 2:
        continue

    is_prime = True
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            is_prime = False
            break
    
    if is_prime == True:
        answer += 1
print(answer)