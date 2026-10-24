n = int(input())
k = int(input())
prices = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if abs(prices[i] - prices[j]) == k:
            count += 1

print(count) 