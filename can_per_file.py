import re
import math 

def file_to_list(path):
    # opening the file in read mode
    my_file = open(path, "r")
    
    # reading the file
    data = my_file.read()
    
    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data_into_list = data.replace('\n', ' ').split()
    data_into_list = [re.sub('[^a-zA-Z]+', '', x).lower() for x in data_into_list]
    my_file.close()
    return data_into_list


def num_of_cans(path):
    spagehtti_letter = [27, 28, 29, 26, 32, 31, 28, 26, 28, 30, 39, 32, 27, 25, 441, 35, 26, 37, 30, 31, 28, 25, 31, 28,26, 36]
    letters_txt = [0 for i in range(26)]
    spagehtti_letter = [27, 28, 29, 26, 32, 31, 28, 26, 28, 30, 39, 32, 27, 25, 441, 35, 26, 37, 30, 31, 28, 25, 31, 28,26, 36]
    letters_txt = [0]*26
    wordlist = file_to_list(path)
    for sentence in wordlist: 
        for i in range(26):
            letters_txt[i] += sentence.count(chr(97 + i))
    cans_each_letter = [round(letters_txt[i]/spagehtti_letter[i]) + 1 for i in range (26)]
    cans_needed = max(cans_each_letter)

    leftover_spaghettios = [(cans_needed*spagehtti_letter[k]) - letters_txt[k] for k in range(26)]

    print("The number of spaghettio cans needed to do this file is " + str(cans_needed) + " can(s)")
    print("Cost needed to buy cans: $" + str(round(1.39 *cans_needed, 2)))
    print("Num of leftover spaghettios: " + str(sum(leftover_spaghettios)))

if __name__ == "__main__": 
    path = r'C:\Users\alpag\OneDrive\Documents\Al\Coding\Projects\spaghetti\taylor.txt'
    num_of_cans(path)