n = int(input())
sum = 0
for i in range (1,n+1):
    if n % i == 0 and i % 2 == 0:
        sum += i

print(sum)