# 归并排序

def merge_sort(lst):

    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left if left else right)
    return merged


if __name__ == '__main__':
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(merge_sort(lst))

# complexity: O(nlogn)