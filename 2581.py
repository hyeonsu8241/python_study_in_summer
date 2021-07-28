m = int(input())
n = int(input())
k = 0
num = [0] * 256
st = m
if 1 <= n and n <= 10000 and 1 <= m and m <= 10000:
    if st <= n:
        while st <= n:
            for j in range(2, st):
                if st % j == 0:
                    st += 1
                    break
                else:
                    num[k] = st
                    k += 1
                    st += 1
                    

        sum = 0
        for i in range(len(num)):
            sum += num[i]
            print(num[i])

print(sum)
print(num[0])