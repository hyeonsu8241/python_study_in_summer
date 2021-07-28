n = int(input())
if (1 <= n and n <= 20):
    a = 0
    b = 1
    c = 1
    count = 2
    while count <= n:
        c = a + b
        a = b
        b = c
        count += 1
    print(c)

elif n == 0:
    c = 0
    print(c)

elif n == 1:
    c = 1
    print(c)