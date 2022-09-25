def Bubble_sort(arr):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                a = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = a
    return(arr)

print('Введите длину массива:')
n = int(input())
print('Введите массив:')
arr = [int(i) for i in input().split()]

print(arr)
Bubble_sort(arr)
print(arr)