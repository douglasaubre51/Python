num=int(input("enter a no:"))
x=0
y=1

if(num==0):
    print(num)
elif(num==1):
    print(num-1)
    print(num)
else:
    print("0\n1")
    for i in range(num):
        temp=x+y
        print(temp)
        x=y
        y=temp