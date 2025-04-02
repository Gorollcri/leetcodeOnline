def alg(nums, k):
    n = len(nums)
    ptr = -1
    res = []
    cur = 0

    for i in range(n):
        while ptr + 1 < n:
            cur += nums[ptr + 1]
            ptr += 1
            print(i, ptr, cur)
            if cur == k:
                res.append(i)
                cur -= nums[i]
                break
            while cur > k and i < ptr:
                cur -= nums[i]
                i += 1
                if cur == k:
                    res.append(i)

                    cur -= nums[i]
                    i += 1
                    break


    return len(res), res

def test():
    nums, k = [-1, -1, 1], 0 
    print(alg(nums, k))

test()