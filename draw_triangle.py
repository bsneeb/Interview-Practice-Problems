
def drawTriangle(h):
    ''' Draw a triangle of height h '''
    ct = 1
    for i in range(1,h+1):
        print("*"*i+"\n")
        
if __name__ == "__main__":
    # Param: Height of triangle
    drawTriangle(4)