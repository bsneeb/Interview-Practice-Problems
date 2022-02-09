
def buildTriangle(h):
    ''' Draws a triangle out of numbers with height h '''

    count = 1
    count1 = 0
    for i in range(h):
        count1 += 1
        if (i < h/2):
            for j in range(i):
                print(count, end="")
                count += 1
            print("\n")
        else:
            count = count1
            for j in range(h-i):
                print(count, end="")
                count += 1
            count = count1 - (h - i) + 1
            print("\n")


if __name__ == "__main__":
    buildTriangle(8)