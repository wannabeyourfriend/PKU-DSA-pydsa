# 实现希尔排序
def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue

import time
arr = [3, 1, 2] * 1000
start_time = time.time()  # 开始计时
shell_sort(arr)
end_time = time.time()  # 结束计时
print(f"希尔排序运行时间: {end_time - start_time} 秒")

# complexity: O(n^x), x ∈ (1.3, 2)