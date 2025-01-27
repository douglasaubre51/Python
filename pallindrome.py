num=int(input("enter a no : "))
number=num
reverse=0
temp=0

while num!=0 :
    temp=num%10
    reverse=reverse*10+temp
    num=int(num/10)

if(number==reverse):
    print(f"the no is a pallindrome:{reverse}")
else:
    print(f"the no is not a pallindrome:{reverse}")