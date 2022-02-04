



arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

count = 0;

for i in arr:

    for j in arr:
        if i < j:
            count+=1
            print(f"i: {i}    j: {j}")
        

