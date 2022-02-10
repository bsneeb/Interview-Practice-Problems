
def prodThree(x):
    total = 1
    for i in range(0, 3):
        total = x[i] * total
    print(total)


def largestProd(x):

    total = 0
    newTotal = 0

    for i in range(0, len(x)):
        total = x[i]*x[i+1]*x[i+2]

        if newTotal >= total:
            newTotal = total
            print(newTotal)


if __name__ == '__main__':
    nums = [10, -10, 5, 2]
    prodThree(nums)
