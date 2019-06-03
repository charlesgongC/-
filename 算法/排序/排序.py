li = [9,7,5,6,3,2,4,8,1]
# 冒泡
# def BubbleSort(li):
#     for i in range(len(li)):
#         for j in range(len(li)-i-1):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#     return li

# 选择
# def selectSort(li):
#     for i in range(len(li)-1):
#         for j in range(i+1,len(li)):
#             if li[i] > li[j]:
#                 li[i],li[j] = li[j],li[i]
#     return li
# print(selectSort(li))

# def insertSort(li):
#     for i in range(len(li)):
#         tmp = li[i]
#         j = i - 1
#         while j >=0 and li[j]>tmp:
#             li[j+1] = li[j]
#             j -=1
#         li[j+1] = tmp
#     return li
# print(insertSort(li))

# 插入排序
def insertSort(li):
    for i in range(1,len(li)):
        tmp = li[i]
        j = i
        while j > 0 and li[j-1] > tmp:
            li[j] = li[j-1]
            j -= 1
        li[j] = tmp
    return li
# insertSort(li)
# print(li)


# 快速排序
def quickSort(li,left,right):
    if left > right: return
    l = left
    r = right
    tmp = li[l]
    while l < r:
        while l < r and li[r] >= tmp:
            r -= 1
        li[l] = li[r]
        while l < r and li[l] <= tmp:
            l += 1
        li[r] = li[l]
    li[l] = tmp
    quickSort(li,left,l-1)
    quickSort(li,l+1,right)

# quickSort(li,0,len(li)-1)
# print(li)


# 归并排序
def merge(li,low,mid,high):
    i = low
    j = mid + 1
    ltmp = []
    while i <=mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i = i + 1
        else:
            ltmp.append(li[j])
            j = j + 1
    while i <= mid:
        ltmp.append(li[i])
        i = i + 1
    while j <= high:
        ltmp.append(li[j])
        j = j + 1
    li[low:high + 1] = ltmp

def mergeSort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(li, low, mid)
        mergeSort(li, mid + 1, high)
        print('归并之前:', li[low:high + 1])
        merge(li, low, mid, high)
        print('归并之后:', li[low:high + 1])

# mergeSort(li,0,len(li)-1)
# print(li)

# 希尔排序
def shell_sort(li):
    gap = len(li)//2
    while gap > 0:
        for i in range(gap,len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp
        gap //= 2
    return li

print(shell_sort(li))
