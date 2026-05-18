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
def find_common_words(count1, count2): # this function finds word that appear in both essays using set intersection
    set1 = set(count1.keys()) # unique words from essay 1
    set2 = set(count2.keys()) # unique words srom essay 2

    common = set1 & set2 # intersection btn two essay

    print(f"Total common words found: {len(common)}")
    print(f"{word:<20 } {'essay1 Count':>15} {'essay2 Count':>15}")
    print(f" {'-'*20} {'-'*15} {'-'*15}")
     for word in sorted(common): # sorted() makes output alphabetical and readable
        print(f"{word:<20} {count1[word]:>15} {count2[word]:>15}")

     return common    
            
            
  
