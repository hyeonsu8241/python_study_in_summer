from io import IncrementalNewlineDecoder


T = int(input())
n = int(input())

if 1 <= T and T <= 10 and 1 <= n and n <= 1000000:
   binary_number = bin(n)
   binary_number = str(binary_number)
   k = -2
   for i in binary_number:
      if i == str(T):
         print(k, end = ' ')
      k += 1