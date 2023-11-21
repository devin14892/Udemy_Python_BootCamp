# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


set1 = (20,10) 
set2 = (12,8)
set3 = (2,3)


def makes_twenty(numbers):
    #tubles = [int(x) for x in numbers]
    #print(type(numbers), "<-- is the numbers type", "\n", type(tubles), "<-- this is the tubles type")

      
    if numbers[0] + numbers[1] == 20:
        print('True', numbers[0], '+', numbers[1], 'equals 20') 
    elif numbers[0] == 20 or  numbers[1] == 20:
        print("True")
    else:
        print('False')

    pass





makes_twenty(set1)
makes_twenty(set2)
makes_twenty(set3)

