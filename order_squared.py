
def square(x):
    '''' Given a unsorted list, return a sorted list with squared values '''
    newList = []
    for i in range(0, len(x)):
        newList.append((x[i])**2)
    newList.sort()
    print(newList)


if __name__ == '__main__':
    nums = [-9, -2, 0, 2, 3]
    square(nums)
