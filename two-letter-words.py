import re
import functools

twoletters = re.compile("^..$")

def string_compare(s1, s2):
    if s1 < s2:
        return -1
    
    if s2 > s1: 
        return 1
    
    return 0


def backward_compare(w1, w2):
    return string_compare(w1[1], w2[1]) or string_compare(w1[1], w2[1]) 

def write_words(filename, arr):
    with open(filename,'w') as file:
        for word in arr:
            file.write(word + "\n")

with open('legal-words.txt','r') as file:
    words = []
    for line in file:
        word = line.strip().upper()
        if twoletters.match(word):
            words.append(word)
    

    write_words("two-letter-words.txt", words)

    words.sort(key=functools.cmp_to_key(backward_compare))
    write_words("two-letter-words-back-sorted.txt", words)

    print("done")
 