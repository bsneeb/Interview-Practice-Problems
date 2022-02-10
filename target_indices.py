
def targetIndices(arr, target):
    ''' Given array (arr) sort the array then return what positions the target is occupying. '''
    arr.sort()
    newlist = [x-1 for x in arr if x == target]
    print(newlist)


if __name__ == '__main__':
    arr = [1, 2, 5, 2, 3]
    targetIndices(arr, 3)
