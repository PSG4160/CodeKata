S = int(input())

while S:
    answer = []
    a = list(map(str, input().split()))
    for i in a[1]:
        answer.append(i*int(a[0]))
    print(''.join(answer))
    S -= 1