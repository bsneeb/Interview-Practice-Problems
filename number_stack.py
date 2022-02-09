
def buildStack(l, h):
    ''' Build a stack of triangles of length l and height h '''

    for i in range(1, h + 1):
        print(str(i) * l + "\n", end="")

if __name__ == "__main__":
    buildStack(5,6)
