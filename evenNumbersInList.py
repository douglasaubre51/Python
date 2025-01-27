list1=[2,5,2,1,2,4]

count=0

for i in list1:
    if i%2==0:
       count+=1

print(f'no of even numbers in {list1} : {count}')