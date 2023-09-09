group = [(2,4), (2,5), (16,8), (21,7)]

def lesser_of_two_events(set):
    for x,y in set:
        if x % 2 == 0 and y % 2 == 0:
            if x > y:
               print(y,' is smaller')
            else:
               print(x,' is smaller')
        else:
            if x > y:
               print(x,' is larger')
            else:
               print(y,' larger')


def lesser_of_two(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)


lesser_of_two_events(group)
