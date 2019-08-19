def findMin(nums):
    # 首先考虑边界条件
    if not nums or len(nums) == 0:
        raise Exception("error array")
    head = 0
    tail = len(nums) - 1
    indexMid = head

    while (nums[head] >= nums[tail]):
        # 找到两个子数组的分界线
        if head == tail + 1:
            indexMid = tail
            break
        indexMid = head + (tail - head) // 2

        # 三个元素相等，无法判断该移动哪个指针
        if (nums[head] == nums[indexMid]) and (nums[tail] == nums[indexMid]):
            return findMinInorder(nums, head, tail)
        if (nums[head] <= nums[indexMid]):
            head = indexMid
        elif (nums[indexMid] <= nums[tail]):
            tail = indexMid
    return nums[indexMid]


def findMinInorder(nums, head, tail):
    # 按序找最小的元素
    res = nums[head]
    for i in range(head, tail+1):
        if res >= nums[i]:
            res = nums[i]
    return res
