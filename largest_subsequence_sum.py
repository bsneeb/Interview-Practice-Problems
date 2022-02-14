

def maxSubsequence(nums, k):
    ''' Returns the max subsequence of k elements in array nums '''

    if len(nums) < k:
        print("K is greater than len(nums). Abort")
        return

    nums.sort()
    tot = 0
    for i in range(0, k):
        tot += nums[-1-i]
    print(tot)


if __name__ == '__main__':

    nums = [10, 3, 4, 62, 1, 0, 22, 6, 2]
    maxSubsequence(nums, 2)
