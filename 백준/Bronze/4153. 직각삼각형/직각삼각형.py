while True:
    x,y,z = map(int, input().split())

    if x == 0 and y == 0 and z == 0:
        break
    
    a, b, c = sorted([x,y,z])
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")