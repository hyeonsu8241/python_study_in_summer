A, B = map(int, input().split())
num = [0] * 256
k = 0
sum = 0
if 1 <= A and A <= 1000 and A <= B and 1 <= B and B <= 1000:
    for i in range(1, 1000):
        for j in range(k, i):
            num[j] = i
            k += 1

for i in range(A, B):
    sum += num[i]

print(sum)