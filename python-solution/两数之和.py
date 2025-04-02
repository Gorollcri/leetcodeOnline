def alg(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == target:
                return (i, j)
#  actually n_square time

def alg1(nums, target):
    hashtable = dict()
    for idx, num in range(len(nums)):
        1


def test_alg():
    assert alg([2, 7, 11, 15], 9) == (0, 1), 'Test Case 1 Failed'
    assert alg([3, 2, 4], 6) == (1, 2), 'Test Case 2 Failed'
    assert alg([3, 3], 6) == (0, 1), 'Test Case 3 Failed'
    assert alg([3, 2, 3], 6) == (0, 2), 'Test Case 4 Failed'
    assert alg([3, 2, 3], 7) == None, 'Test Case 5 Failed'
    print('All test cases passed')

if __name__ == '__main__':
    test_alg()