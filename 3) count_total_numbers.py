num = int(input())

total = 0

while num > 0:
    n = num % 10
    num = num // 10

    total += 1

print(total)