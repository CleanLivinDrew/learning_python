"""testing functions"
"""

x = 2
y = 1


if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

def countdown(n):
    """countdown function"""
    if n <= 0:
        print('blastoff!')
    else:
        print(n)
        countdown(n-1)


countdown(10)
