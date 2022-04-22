def capital_indexes(string):
    caps=[]
    for index,letter in enumerate(string):
        if letter.isupper():
            caps.append(index)

    return caps


print(capital_indexes('HeLlo'))
print(capital_indexes('This Is a TesT on CapitAl letters' ))
print(capital_indexes('This Is a another TesT on CapitAl letters usInf capiTal Index Function' ))
