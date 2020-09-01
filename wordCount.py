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

    cur_file.close()
    output_file.close()


file = input("What file would you like to read? ")
#We will store the users file in this string
wordCount(file)
