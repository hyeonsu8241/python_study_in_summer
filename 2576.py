nums = [0] * 7
odds = [0] * 7
k = 0
sum = 0
for i in range(7):
    nums[i] = int(input())
    if nums[i] < 1 or nums[i] > 100:
        break

for i in nums:
    if i % 2 == 1:
        odds[k] = i
        sum += i
        k += 1
odds.sort()
if sum == 0:
    print(-1)
elif sum != 0:
    print(sum)
    print(odds[7 - k])