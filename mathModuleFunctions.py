import math

def mathFunctions(a,b):
    print(f"ceil of {a}:{math.ceil(a)}")
    print(f"floor of {a}:{math.floor(a)}")
    print(f"factorial of {b}:{math.factorial(b)}")
    print(f'value of pi:{math.pi}')
    print(f'value of sin 90:{math.sin(90)}')
    print(f'result of {a}^{b}:{math.pow(a,b)}')
    print(f'squareroot of {b}:{math.sqrt(b)}')
    print(f'log of {b}:{math.log(b)}')

a=float(input('enter a floating point number:'))
b=int(input('enter an integer number:'))
mathFunctions(a,b)