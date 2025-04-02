def alg(nums):
    left = 0
    right = len(nums) - 1
    volumn = 0

    while right != left:
        v_temp = min(nums[right], nums[left]) * (right - left)
        volumn = max(volumn, v_temp)
        print(f"({nums[left]},{nums[right]})")
        if nums[left] >= nums[right]:
            right -= 1
        else:
            left += 1
    return volumn

def test():
    nums = [1,2,4,3]
    print(alg(nums))

test()