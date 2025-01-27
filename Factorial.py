num=int(input("Enter a number:"))
print(f"factorial of {num} :")

def Factorial(n: int)->int:
    if n==1:
        return n
    else:
        n=n*Factorial(n-1)
    return n

result=Factorial(num)

print(result)