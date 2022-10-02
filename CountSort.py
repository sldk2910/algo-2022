mass = [2, 3, 2, 4, 1, 2, 3, 1, 5, 6, 7, 9, 5]
res = [0]*10
for el in mass:
    res[el] += 1
for i in range (len(res)):
    for j in range(res[i]):
        print(i)