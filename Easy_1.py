def last_word_length(s):#function takes a string s
    list_of_words=s.split(" ")



    new_list=[]
    #remove all non words from list
    for i in list_of_words:
        if i!="":
            new_list.append(i)

    #return length of last word
    return len(new_list[-1])


#test
s="luffy is still joyboy"
print(last_word_length(s))