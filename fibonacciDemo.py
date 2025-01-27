#doesnot work
number=int(input("enter no of terms : "))

if(number==0):
    print(number)

elif (number==1):
    print(number)

else:
    print("0\n1")
    
    for i in range(2,number):
        temp=(i-1)+(i-2)
        print(temp)