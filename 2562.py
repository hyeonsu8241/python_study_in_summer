num_input = [0] * 9
save = 0
k = 0
max = 0
for i in range(9):
    num_input[i] = int(input())
    if num_input[i] <= 0 and num_input[i] >= 100:
        break
    if max < num_input[i]: max = num_input[i]

for j in range(9):
    if num_input[j] == max:
        save = j + 1

print(max)
print(save)