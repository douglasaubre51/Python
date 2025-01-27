tuple1=1000,1,-1,3,6,1,4,3,6,312,0

max=0
min=2

for i in tuple1:
    if max<i:
        max=i

    if min>i:
        min=i

print(f'minimum value in {tuple1} : {min}')
print(f'maximum value in {tuple1} : {max}')