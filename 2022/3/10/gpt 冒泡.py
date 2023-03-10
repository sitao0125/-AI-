def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后 i 个元素已经排好，不需要再比较
        for j in range(0, n-i-1):
            # 如果当前元素的个位数大于下一个元素的个位数，或者个位数相等但是当前元素大于下一个元素
            if arr[j] % 10 > arr[j+1] % 10 or (arr[j] % 10 == arr[j+1] % 10 and arr[j] > arr[j+1]):
                # 交换两个元素的位置
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# 读入 n 个数
n = int(input("请输入数字个数："))
arr = []
for i in range(n):
    num = int(input("请输入第%d个数字：" % (i+1)))
    arr.append(num)

# 调用冒泡排序算法，对数组进行排序
arr = bubble_sort(arr)

# 输出排序后的数组
print("排序后的数组为：")
for num in arr:
    print(num, end=' ')
