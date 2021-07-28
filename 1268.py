n = int(input())
num = list()
for i in range(n):
    num[i].randint(1,n)
    print(num[i], end='')

for s in num:
    if s % 2 == 0:
        print(s)