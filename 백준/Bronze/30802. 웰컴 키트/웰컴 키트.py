n = int(input())
Size = list(map(int, input().split()))
T, P = map(int, input().split())

''' 기본적으로 T 장씩 더하기, T와 같거나 작을때, 나머지는 T의 배수보다 작거나 같게해서 배수를 더하기'''
answer = 0
for i in Size:
    answer += (i + T - 1) // T

print(answer)
print(f'{n//P} {n%P}')