x = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != x and low <= high:
    if x > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if a[mid] == x:
    print(mid)
else:
    print(-1)