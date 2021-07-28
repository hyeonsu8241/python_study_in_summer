def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
sum = [0] * t
for i in range(t):
    num = list(map(int, input().split()))
    for j in range(1, num[0] + 1):
        for k in range(2, num[0] + 1):
            if j == k: continue
            sum[i] += gcd(num[j], num[k])
            
for i in range(t):
    print(sum[i])