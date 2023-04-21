
# we want to return all even numbers
def cheeck_even_numbers(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            print(number)
            #even_numbers.append(number)
        else:
            #print(number, "not even")
            pass
    #return even_numbers

list = [1,6,3,8]

cheeck_even_numbers(list)

#print(cheeck_even_numbers(list))
