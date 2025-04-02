def alg(nums, k):
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        max1 = nums[i]
        for j in range(i, i + k):
            max1 = max(max1, nums[j])

        res.append(max1)
    return res

def test():
    nums, k = [1,2,3,4,5,6,7,21,8], 3
    print(alg(nums, k))


test()
