list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]

print([(i, i) for i in list_a if i in list_b])