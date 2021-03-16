type = input()
pi = 3.14
if type == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a+b+c)/2)
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif type == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a*b)
elif type == 'круг':
    r = int(input())
    print(pi*(r**2))