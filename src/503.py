import time

# 冒泡排序
def bubble_sort(arr):
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        # print(arr)

arr = [1, 2, 3] * 1000

start_time = time.time() # 开始计时
bubble_sort(arr)
end_time = time.time()  # 结束计时

print(f"冒泡排序运行时间: {end_time - start_time} 秒")

# 冒泡排序的改进：某一趟扫描没有数据交换，则说明已经排好序了
def short_bubble_sort(arr):
    exchange = True
    passnum = len(arr) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                exchange = True
                arr[i], arr[i+1] = arr[i+1], arr[i]
        passnum -= 1
        # print(arr)

arr =  [1, 2, 3] * 1000

start_time = time.time()  # 开始计时
short_bubble_sort(arr)
end_time = time.time()  # 结束计时

print(f"改进冒泡排序运行时间: {end_time - start_time} 秒")

# complexity: O(n^2)

# 选择排序
def selection_sort(arr):
    for fillslot in range(len(arr)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot+1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
        arr[fillslot], arr[position_of_max] = arr[position_of_max], arr[fillslot]
        print(arr)

arr = [i for i in range(10, 0, -1)]
print(arr)
selection_sort(arr)

# complexity: O(n^2)