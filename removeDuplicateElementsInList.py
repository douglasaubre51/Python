numberList=[1,4,4,4,1,3,0,10, 20, 50, 40, 50, 60, 70, 80, 90, 10, 10, 20, 30]

print('original list:')
for i in numberList:
    print(i)

numberList.sort()
i=0
counter=0

while(i<(len(numberList))-1):
    if(counter>0):
        del numberList[i]
        counter-=1

    if(numberList[i]==numberList[i+1]):
        counter+=1
    
    i+=1
    

print('modified list:')
for i in numberList:
    print(i)