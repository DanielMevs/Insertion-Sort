arr = [3,44,5,47,15,36,26,27,2,46]
print("array = ", arr)

sorted_elmt = arr[0]
i = 1
temp = 0
n = len(arr)
while i < n:
    current = arr[i]
    j = i - 1
    while j >= 0:
        if arr[i] < arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            print(arr)
        j = j -1
    i = i + 1


