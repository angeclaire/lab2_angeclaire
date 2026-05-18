"""
  PLAGIARISM DETECTOR APPLICATION PROJECT
"""

import string # Used to remove punctuation from words
def load_essay(filename): #this function reads a text and returns a list of cleaned,lowercase words.

    try:
        with open(filename, "r") as file:
             content = file.read()
            # convert to lowercase and split into individual words
            words = content.lower().split()
            # remove punctuation from each word using str.strip
            cleaned_words = [word for word in cleaned_words if word]
            return cleaned_words
    except FileNotFoundError:
        print(f"[error] File '{filename}' was not found. please check the filename.")
        return[]
def count_words(word_list): #this function counts how many times each word appears in list.
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1 # increment count
        else:
            word_count[word] = 1 # start count at 1
    return word_count


            
            
  
