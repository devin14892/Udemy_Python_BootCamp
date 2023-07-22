def myfunc(*args):
    myList = []
    for x in args:
        if x % 2 == 0:
            myList.append(x)
        
    return myList

print(myfunc(2,7,11,8))