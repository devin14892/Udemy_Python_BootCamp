
list1 = ([1,2,4,0,0,7,5])
list2 = ([1,0,2,4,0,5,7])
list3 = ([1,7,2,0,4,5,0])


def spy_game(numbers):
    numberslist = [int(x) for x in numbers]
    key = []
    awn = [0,0,7]
    for i in numberslist:
        if i in [0, 7]:
        # also works --> if i == 0 or i == 7:
            key.append(i)
    
    if key == awn:
        print('match found', key)





    pass


spy_game(list1)
spy_game(list2)
spy_game(list3)