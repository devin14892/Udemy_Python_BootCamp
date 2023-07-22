"""
def alternate_case(word):
    SkyScrapperCase = ''.join(x + y for x, y in zip(word[0::2].upper(), word[1::2].lower()))
    return SkyScrapperCase
"""
def myfunc(x):
    newString=""
    for i in range (len(x)):
        if(i%2==0):
            newString+=x[i].upper()
        else:
            newString+=x[i].lower()       
    return newString

print(myfunc("hello"))

