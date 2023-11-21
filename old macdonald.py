#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

Name1 = "Henry"
Name2 = "macdonald"
Name3 = "david"



def firstAndFourth(name):

    CapName = name[0:1].upper() +  name[1:3] + name[3:4].upper() + name[4:]
    print(CapName)

    pass

firstAndFourth(Name1) 
firstAndFourth(Name2)
firstAndFourth(Name3)