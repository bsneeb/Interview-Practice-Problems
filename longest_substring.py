''' Find the longest substring without repeating characters '''


def solve(str):

    temp = []
    hi_count = 0
    highest_count = 0

    for x in str:
        if x in temp:
            print(f"We got a repeating char {x}")
            if highest_count < hi_count:
                print(f"Highest count: {highest_count}")
                highest_count = hi_count
                hi_count = 1
            temp = []
            temp.append(x)

        elif x not in temp:
            temp.append(x)
            print(temp)
            hi_count += 1

    print(f"Length: {highest_count}")


if __name__ == '__main__':

    # Case 1
    str = "abcabcbb"
    solve(str)

    # Case 2
    str = "bbbbb"
    solve(str)

    # Case 3
    str = "pwwkew"
    solve(str)
