def alg(nums):
    cnt = 0
    for i in nums:
        if i == 0:
            cnt += 1
    nums = [x for x in nums if x != 0]
    for j in range(cnt):
        nums.append(0)
    return nums

def alg1(nums):
    n = len(nums)
    right = left = 0
    while right < n:
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        right += 1
    return nums

def test():
    nums = [0,1,0,3,12]
    print(alg1(nums))

test()