def wordCount(file):
    cur_file = open(file)
    hash_table ={}

    current_word = ''
    for line in cur_file:
        for word in line:
            word = word.lower()
            if word.isalpha():
                current_word += word
            else:
                if current_word in hash_table:
                    hash_table[current_word] += 1
                else:
                    hash_table[current_word] = 1
                current_word = ''

    output_file = open("output.txt", "w")
    for key in sorted(hash_table.keys()):
        output_file.write(key+" "+str(hash_table[key])+"\n")
        #Formats it in the way the key text files are

    cur_file.close()
    output_file.close()

def rmFirstLine():
    with open("output.txt", "r") as file:
        data = file.read().splitlines(True)
    with open("output.txt", "w") as file_out:
        file_out.writelines(data[1:])


file = input("What file would you like to read? ")
wordCount(file)
rmFirstLine() #For some reason I had a weird first line
