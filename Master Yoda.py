words1 = "I am home"
words2 = "We are ready"
words3 = "I knew your father"


def master_yoda(sentance):
    sentancelist = sentance.split(" ")
    print(sentancelist)
    #reversed_sentance = sentancelist[::-1]
    sentancelist.reverse() #https://realpython.com/python-reverse-list/
    print(sentancelist)
    
    #rint(reversed_sentance)
       
    pass



master_yoda(words1)
master_yoda(words2)
master_yoda(words3)