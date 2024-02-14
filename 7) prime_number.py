import math

start_limit = int(input())
end_limit = int(input())

numbers = [i for i in range(start_limit, end_limit+1)]

for num in numbers:
    flag = 0
    if num <= 1:
        continue
    
    elif num == 2:
        print('2', end=' ')

    elif num > 2:
        if num % 2 == 0:
            continue

        else:
            sqrt = math.ceil(num**0.5)
            # print(sqrt)

            for div in range(3, sqrt+1, 2):
                if num % div == 0:
                    flag = 1
                    continue

            if flag == 0:
                print(num, end= ' ')
    

