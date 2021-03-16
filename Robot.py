n = int(input())
if 0 <= n <= 1000:
    if n%10 == 1 and n%100 != 11:
        print(n, 'программист')
    elif n%10 == 0 or n%10 == 5 or n%10 == 6 or n%10 == 7 or n%10 == 8 or n%10 == 9 or n%100 == 11 or n%100 == 12 or n%100 == 14 or n%100 == 13:
        print(n, 'программистов')
    elif n%10 == 2 or n%10 == 3 or n%10 == 4:
        print(n, 'программиста')


