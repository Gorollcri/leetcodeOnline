def alg(s, p):
    n = len(s)
    res = []

    if len(p) > n:
        return res
    
    for i in range(n):
        rl = i
        table = list(p)

        if s[i] not in table:
            continue

        while rl < n and s[rl] in table:
            table.remove(s[rl])
            rl += 1
        if len(table) != 0:
            continue
        else:
            res.append(i)
    return res
#   这种方法还有很多可以剪枝的地方，时间复杂度很高
#   官方使用字母表哈希，计算
def test():
    s, p = "aaaaaa", "aa"
    print(alg(s, p))


test()