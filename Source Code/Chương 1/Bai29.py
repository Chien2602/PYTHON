l = []
n = int(input())
for i in range (1,n):
    if n % i == 0 and i % 2 == 1:
        l.append(i)

print(max(l))