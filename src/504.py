import time
# 插入排序的实现
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [1, 2, 3] * 1000
start_time = time.time()  # 开始计时
insert_sort(arr)
end_time = time.time()  # 结束计时
print(f"插入排序运行时间: {end_time - start_time} 秒")

# complexity: O(n^2)
