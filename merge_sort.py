def merge(arr, start, mid, end):
    left_length = mid - start + 1
    # left_arr = []
    # for i in range(left_length):
    #     left_arr.append(arr[start + i])

    left_arr = [arr[start + i] for i in range(left_length)] # The pythonic way

    right_length = end - mid
    # right_arr = []
    # for i in range(right_length):
    #     right_arr.append(arr[mid + 1 + i])

    right_arr = [arr[mid + 1 + i] for i in range(right_length)] # The pythonic way

    i = j = 0
    k = start

    while(i < left_length and j < right_length):
        if(left_arr[i] < right_arr[j]):
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while(i < left_length):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while(j < right_length):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if (start == end):
        return
    mid = (start + end) // 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)


arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)

merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
