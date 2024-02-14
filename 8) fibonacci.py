total = 0

while total <= 10:
    if total == 0:
        n1 = 0
        print(n1, end=' ')
    elif total == 1:
        n2 = 1
        print(n2, end=' ')
    else:
        n2, n1 = n2 + n1, n2
        print(n2, end=' ')

    total += 1
        