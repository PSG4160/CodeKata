a = int(input())
b = list(map(int, input().split()))

if a == len(b):
    print(f"{min(b)} {max(b)}")