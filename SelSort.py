def Sel_sort(arr):
    for i in range(0, n - 1):
        s = i
        for j in range(i + 1, n):
            if arr[j] < arr[s]:
                s = j
                buff = arr[i]
                arr[i] = arr[s]
                arr[s] = buff
    return(arr)


print('Введите длину массива:')
n = int(input())
print('Введите массив:')
arr = [int(i) for i in input().split()]

print(arr)
Sel_sort(arr)
print(arr)