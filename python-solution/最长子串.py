def slide_windows(s):
    n = len(s)
    rl = -1
    max_len = 0


    for i in range(n):
        l = 1
        res = set()
        res.add(s[i])
        rl = i
        while rl < n-1:

            if s[rl+1] not in res:
                res.add(s[rl+1])
                l += 1
                rl += 1
            else:
                break
        max_len = max(l, max_len)

    return max_len


def slide_window2(s):
    n = len(s)
    res = set()
    ptr = -1
    max_len = 0

    for i in range(n):
        if i > 0:
            res.remove(s[i - 1])
        while ptr + 1 < n and s[ptr + 1] not in res:
            res.add(s[ptr + 1])
            ptr += 1
            max_len = max(max_len, ptr - i + 1)


    return max_len


def test():
    strs = "abcadcbeab"
    print(slide_windows(strs))


test()