a = int(input())
b = input()

answer = 0

if len(b) == a:
    for i in b:
        answer += int(i)
    print(answer)