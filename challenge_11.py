def largest_difference(lista):
    
    min = lista[0]
    max = lista[0]
    
    for num in lista:
        if min > num:
            min = num
        elif max < num:
            max = num
    dif = max - min

    return dif
        
print(largest_difference([2,1,5,4,8,3,10]))