
def printRect(w, h):
    ''' Draw a rectangle of width w and height h'''
    for i in range(0,h):
        print("*" *w)
    
if __name__ == "__main__":
    printRect(3,7)
