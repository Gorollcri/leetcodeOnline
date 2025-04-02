def alg(nums):
    nums = sorted(nums)
    max_cnt = 1
    cnt = 1
    for idx, _ in enumerate(nums):
        if nums[idx] == nums[idx-1]:
            continue
        if idx != 0 and nums[idx] == nums[idx-1] + 1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        elif nums[idx] != nums[idx-1] + 1:
            cnt = 1
    return max_cnt if len(nums) != 0 else 0

def test():
    nums = []
    print(alg(nums))

test()