
print('#'*100, "\n")

st = 'Print only the words that start with s in this sentence'

mylist = st.split()


for word in mylist:
    if word[0] =='s':
        print(word) 

print('#'*100, "\n")
####################################################################################
'''
Another option would be to do the following:
Numbers = list(range(0,11,2)) 
    instead of
Numbers = range(0,11,2)

'''


Numbers = range(0,11,2)
EvenNumberList = [n for n in Numbers]
print(EvenNumberList) 

print('#'*100, "\n")
####################################################################################
"""
Another way
[x for x in range(1,51) if x%3 == 0]

"""
NumberList = range(51)
FilledList = [n for n in NumberList]
#create the list outside of the loop or it sets it back to empty everytime
DivList = []
for num in FilledList:
    if num %3 == 0:
        DivList.append(num)

print('#'*100, "\n")
####################################################################################
"""
for word in Newst.split():

"""
Newst = 'Print every word in this sentence that has an even number of letters'

WordList = Newst.split() #dont forget the () or you just get a memory location
for wordy in WordList:
    if len(wordy) %2 ==0:
        print(wordy, "<-- is even")

print('#'*100, "\n")
####################################################################################

BigNumList = range(1,101)
ListONums = [n for n in BigNumList]
for q in ListONums:
    if q %3 == 0 and q %5 == 0:
        print(q, "FizzBuzz")
    elif q %3 == 0:
        print(q, " Fizz")
    else:
        if q %5 == 0:
            print(q, " Buzz")

print('#'*100, "\n")
####################################################################################
"""
[word[0] for word in st.split()]
"""
stringy = 'Create a list of the first letters of every word in this string'
stringyList = stringy.split()

FirstLetters = []

for item in stringyList:
    first = item[0]
    FirstLetters.append(first)

print(FirstLetters)

print('#'*100, "\n")