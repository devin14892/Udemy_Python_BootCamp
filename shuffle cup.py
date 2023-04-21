from random import shuffle


mylist = [' ', 'O',' ']
repeat = "\n""...shuffeling..."

print("Here is where the ball is currently", "\n", mylist, repeat * 3)

shuffle(mylist)

guess = input("Guess where the cup is now, 1, 2 or 3?")


def guess_check(guess):
    yes = "You got it correct"
    no = "nope, try again"
    
    
    if guess == "1":
        if mylist[0] == "O":
            print(yes)
        else:
            print(no)
    elif guess == "2":
        if mylist[1] == "O":
            print(yes)
        else:
            print(no)
    else:
        if mylist[2] == "O":
            print(yes)
        else:
            print(no)

print("\n","New shuffle",mylist,"and you guessed", guess)

guess_check(guess)

       