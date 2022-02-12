
def subarrayAvg(nums, k):
    '''' 
    returns a new array of average of k places to left and right. If runs out of bounds, that place in the array is -1.
    Ex:
    [1, 2, 3, 4, 5, 6, 7, 8] k = 2
      |____|_____|   ---> k*2+1 range for 3
    [-1 -1 3  4  5  6 -1 -1]
    '''

    avgs = []

    for x in range(0, len(nums)):

        avg = 0
        if x >= k and x < (len(nums) - k):

            for j in range(0 - k, k+1):
                avg += nums[x + j]

            temp = avg//((k*2) + 1)
            avgs.append(temp)
            temp = 0
        else:
            avgs.append(-1)

    print(avgs)


if __name__ == '__main__':

    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    subarrayAvg(nums, 2)
