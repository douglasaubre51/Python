dictionary1={
    'model':'sedan',
    'color':'white'
}

dictionary2={
    'brand':'audi',
    'year':2000
}

print(f'dictionary1 : {dictionary1}')
print(f'dictionary2 : {dictionary2}')

dictionary1.update(dictionary2)
print(f'merged dictionary : {dictionary1}')