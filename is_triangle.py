

def is_triangle(a, b, c):
    """function to calc if triangle"""

    a = int(a)
    b = int(b)
    c = int(c)
    if a > b + c or b > a + c or c > a + b:
        print("No")
    else:
        print("Yes")


def triangle_input():
    """function that takes user input for triangle calc"""
    print("Enter side a dimension:")
    side_a = input()
    print("Enter side b dimension:")
    side_b = input()
    print("Enter side c dimension:")
    side_c = input()
    side_a = int(side_a)
    side_b = int(side_b)
    side_c = int(side_c)

    is_triangle(side_a, side_b, side_c)


triangle_input()


