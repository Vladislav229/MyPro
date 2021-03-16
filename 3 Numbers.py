a = int(input())
b = int(input())
c = int(input())
if a>c and a>b:
    max = a
    if b>c:
        min = c
        mid = b
    else:
        min = b
        mid = c
    print(max)
    print(min)
    print(mid)
elif b>c and b>a:
    max = b
    if a>c:
        min = c
        mid = a
    else:
        min = a
        mid = c
    print(max)
    print(min)
    print(mid)
elif c>a and c>b:
    max = c
    if b>a:
        min = a
        mid = b
    else:
        min = b
        mid = a
    print(max)
    print(min)
    print(mid)
elif a==c and a==b:
    max = a
    min = b
    mid = c
    print(max)
    print(min)
    print(mid)
elif a == c and (b > c or b > a):
    max = b
    min = a
    mid = c
    print(max)
    print(min)
    print(mid)
elif a == b and (c > a or c > b):
    max = c
    min = a
    mid = b
    print(max)
    print(min)
    print(mid)
elif a == c and (b < c or b < a):
    max = a
    min = b
    mid = c
    print(max)
    print(min)
    print(mid)
elif a == b and (c < a or c < b):
    max = a
    min = c
    mid = b
    print(max)
    print(min)
    print(mid)
elif c == b and (a > c or a > b):
    max = a
    min = b
    mid = c
    print(max)
    print(min)
    print(mid)
elif c == b and (a < c or a < b):
    max = c
    min = a
    mid = b
    print(max)
    print(min)
    print(mid)
