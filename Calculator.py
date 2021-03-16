a = float(input())
b = float(input())
Operation = input()
if Operation == '/' :
    if b!= 0:
        print(a/b)
    else:
        print('Деление на 0!')
if Operation == '+':
    print(a+b)
if Operation == '-':
    print(a-b)
if Operation == 'mod':
    if b!=0:
        print(a%b)
    else:
        print('Деление на 0!')
if Operation == '*':
    print(a*b)
if Operation == 'pow':
    print(a**b)
if Operation == 'div':
    if b!= 0:
        print(a//b)
    else:
        print('Деление на 0!')