num=int(input("Enter a number:\n"))

def Fibonacci(n: int)->int:
    if(n<=1):
        return n

    else:
        return (Fibonacci(n-1))+(Fibonacci(n-2))

print(f"the fibonacci numbers till {num} is :")

for i in range(num):
    print(Fibonacci(i),end=" ")