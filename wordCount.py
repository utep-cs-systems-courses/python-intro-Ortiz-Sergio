def wordCount(file):
    #Checking if we can open and view the file
    cur_file = open(file)
    for line in cur_file:
        for word in line:
            print(word)


file = input("What file would you like to read? ")
#We will store the users file in this string
wordCount(file)
