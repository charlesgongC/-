def bucketSort(nums):
    max_num = max(nums)
    bucket = [0]*(max_num+1)

    for i in nums:
        # 放入桶中
        bucket[i] += 1
    # 存储排好序的元素
    sort_nums = []
    for j in range(len(bucket)):
        if bucket[j]!=0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums

nums =[3,4,6,3,6,4,5,8,6,3,4,5,6,2,8,2,9,1,2]

print(bucketSort(nums))