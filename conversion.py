def convert(celsiusList):
    farenList = []
    for temp in celsiusList:
        F = ((temp*9)/5)+32
        farenList.append(F)
    return farenList

print convert([32,31,34,33,29,35,30])
