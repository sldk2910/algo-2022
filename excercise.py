mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input())
for i in range(n):
    sum = 0
    l = int(input())
    r =  int(input())
    for j in range(l, r+1):
        sum += mass[j]
    print(sum)
