n = int(input())

if n >= 3:
    print('*' * n)
    for i in range(1, n - 1):
        print('*',' '*(n - 4), '*')
    print('*' * n)