# boolean
import math

def Main():
    print(False == 0)
    print(True == 1)
    print(True + True + False)
    print(True + False + False)
    print(False + False + True)
    print(True - True)
    print(- False)
    print(not False)
    print(not True)
    # 'None' is the 'void' of python. It is NOT like 0 nor an empty container
    # 'None' has its own type - 'None' also

    # Logical operators
    print(True and True)
    # continue the other day
    # 20.12.2020 . The other day has   come.
    print(3 and 0)
    print(3 and 10)
    print(0 and 3)
    # The expression x and y first evaluates x
    # if x is false, its value is returned
    # otherwise, y is evaluated and the resulting value is returned.

    print(4 or 0)
    print(0 or 4)
    print(10 or 20 or 30 or 10 or 70)
    print(10 or (20 or 30) or 10 or 70)
    print(0 or (0 and 30) or 10 or 70)

    # The expression x or y first evaluates x
    # if x is true, its value is returned
    # otherwise, y is evaluated and the resulting value is returned.

    print (None == 0) # Demonstration of difference between None and False/0

    x = None
    y = None
    print (x == y)

    print(None)

    print(not 21)
    print(not -21)
    print(not 1)
    print(not 0)

if __name__ == "__main__":
    Main()