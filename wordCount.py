import sys
import os.path
from os import path

def wordCount(file, output_file):
    if not path.exists(file):
        print("file does not exist, enter a valid file")
        return False
        
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

    output_file = open(output_file, "w")
    for key in sorted(hash_table.keys()):
        output_file.write(key+" "+str(hash_table[key])+"\n")
        #Formats it in the way the key text files are

    cur_file.close()
    output_file.close()
    return True

def rmFirstLine(output_file):
    with open(output_file, "r") as file:
        data = file.read().splitlines(True)
    with open(output_file, "w") as file_out:
        file_out.writelines(data[1:])


if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py input.txt output.txt")
    exit()

file = sys.argv[1]
output_file = sys.argv[2]

if wordCount(file, output_file):
    rmFirstLine(output_file) #For some reason I had a weird first line
