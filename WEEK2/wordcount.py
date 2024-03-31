import string
occurence={}
with open("wordcount.txt", "r") as words:
    read_words=words.read().lower()
    my_list_of_read=read_words.split()
    print(my_list_of_read)
    occurence={}
    for word in range(0, len(my_list_of_read)):
        stripped_words=my_list_of_read[word].strip(string.punctuation)
        if stripped_words not in occurence:
            occurence[stripped_words]=1
        else:
            occurence[stripped_words]= +1

print(occurence)