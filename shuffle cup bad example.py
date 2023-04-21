from random import shuffle


mylist = [' ', 'O',' ']
print("Here is where the ball is currently", "\n", mylist, "\n", "shuffeling" , "\n", "shuffeling" , "\n", "shuffeling" , "\n", )

shuffle(mylist)

guess = input("guess where the cup is now, 1, 2 or 3?")


def guess_check(guess):
    if guess == "1":
        if guess == mylist[0]:
            print("You got it correct", shuffle_list)
        else:
            print("nope")
    elif guess == "2":
        if guess == mylist[1]:
            print("You got it correct", shuffle_list)
        else:
            print("nope")
    else:
        if guess == mylist[2]:
            print("You got it correct", shuffle_list)
        else:
            print("nope")

print("New shuffle",mylist, "\n", "and you guessed", guess)

guess_check(guess)

       