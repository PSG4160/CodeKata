N, M = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

GCD = gcd(N, M)
LCM = (N * M) // GCD
print(GCD)
print(LCM)