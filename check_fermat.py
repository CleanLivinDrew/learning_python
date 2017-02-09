def check_fermat():
    """function to perform the fermat check"""
    print('enter variable a: ')
    a = input()
    a = int(a)
    print('enter variable b: ')
    b = input()
    b = int(b)
    print('enter variable c: ')
    c = input()
    c = int(c)
    print('enter variable n: ')
    n = input()
    n = int(n)

    if n > 2 and (a**n + b**n == c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

check_fermat()
