# https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

def square(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()

def triangle(n):
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(i+1):
            print("* ", end="")
        print()

def triangle(n):
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(i+1):
            print("* ", end="")
        print()

def invertedTriangle(n):
    for i in range(n):
        print(" "*i,end="")
        for j in range(n-i):
            print("* ", end="")
        print()

def rightTriangle0s1s(n):
    for i in range(n):
        for j in range(i+1):
            if (j%2 == 0 and i%2 ==0) or (i%2 != 0 and j%2!=0):
                print(1,"",end="")
            else:
                print("0","",end="")
        print()

def rightTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

def rightTriangleNumber(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num,"", end="")
            num +=1
        print()

def rightTriangleAlfa(n):
    char = ord("A")
    for i in range(n):
        for j in range(i+1):
            print(chr(char),"", end="")
            char += 1
        print()
        char = ord("A")

def rightTriangleAlfaRow(n):
    char = ord("A")
    for i in range(n):
        for j in range(i+1):
            print(chr(char),"", end="")
            
        print()
        char += 1

def invertedRightTriangleAlfa(n):
    char = ord("A")
    for i in range(n):
        for j in range(n-i):
            print(chr(char),"", end="")
            char += 1
        print()
        char = ord("A")

def leftTriangle(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(i+1):
            print(j+1, end="")
        print()

def leftTriangleAlpha(n):
    for i in range(n):
        # spaces
        print(" "*(n-i-1), end="")

        # LEFT increasing characters
        for j in range(i+1):
            print(chr(ord('A') + j), end="")

        # RIGHT decreasing characters
        for j in range(i-1, -1, -1):
            print(chr(ord('A') + j), end="")

        print()

def mTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print(" "*(n-i-1)*2,end="")
        for j in range(i+1):
            print(j+1, end="")
        print()

def SideTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()
  
    y = n-1

    for i in range(y):
        for j in range(y-i):
            print("* ", end="")
        print()

def invertedRightTriangle(n):
    for i in range(n):
        for j in range(n-i):
            print("* ", end="")
        print()

def invertedRightTriangleNum(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end="")
        print()


def rightTriangleNumberCol(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print()

def rightTriangleNumberRow(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1, end="")
        print()


def diamond(n):

    for i in range(n):
        print(" "*(n-i-1)*2,end="")
        for j in range(i*2+1):
            print("* ", end="")
        print()

    for i in range(n):
        print(" "*i*2,end="")
        for j in range((n-i)*2-1):
            print("* ", end="")
        print()
        
        
def revAlphabetStair(n):
    for i in range(n):
        # print spaces
        print(" " * (n - i - 1), end="")

        # starting character = chr(ord('A') + (n - i - 1))
        start = ord('A') + (n - i - 1)

        # loop from start to 'A' + n - 1
        for ch in range(start, ord('A') + n):
            print(chr(ch), end=" ")
        print()

def hollow_double_square(n):
    for i in range(n):
        # left stars
        print("*" * (n - i), end="")

        # middle spaces
        print(" " * (2 * i), end="")

        # right stars
        print("*" * (n - i))


    for i in range(n):
        # left stars
        print("*" * (i + 1), end="")

        # middle spaces
        print(" " * (2*(n - i - 1)), end="")

        # right stars
        print("*" * (i + 1))


def star_hourglass(n):
    # upper half
    for i in range(1, n):
        print("*" * i, end="")
        print(" " * (2*(n - i)), end="")
        print("*" * i)

    # middle full row
    print("*" * (2*n))

    # lower half
    for i in range(n-1, 0, -1):
        print("*" * i, end="")
        print(" " * (2*(n - i)), end="")
        print("*" * i)


def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:         # top or bottom rows
            print("* " * n)
        else:                          # hollow middle rows
            print("* " + "  "*(n-2) + "* ")

def concentric_square(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            # distance from each side
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j

            # layer number (min distance to any border)
            layer = min(top, left, bottom, right)

            print(n - layer, end=" ")
        print()

concentric_square(4)



  