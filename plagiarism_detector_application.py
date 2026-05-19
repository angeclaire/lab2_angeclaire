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
            cleaned_words = [word.strip(string.punctuation) for word in words]
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
    print(f"{'Word':<20} {'essay1 Count':>15} {'essay2 Count':>15}")
    print(f" {'-'*20} {'-'*15} {'-'*15}")
    for word in sorted(common): # sorted() makes output alphabetical and readable
        print(f"{word:<20} {count1[word]:>15} {count2[word]:>15}")

    return common    
def search_word(word,count1, count2):#this function will search for soecific word in both essays.
     if not isinstance(word, str) or not word.strip():
        print("  [ERROR] Please enter a valid word (non-empty text).")
        return False
     
     word = word.strip().lower()  # Normalize the word
 
     found_in_1 = word in count1
     found_in_2 = word in count2

     if not found_in_1 and not found_in_2:
        print(f"  The word '{word}' was NOT found in either essay.")
        return False
 
    # Word found in at least one essay
     count_in_1 = count1.get(word, 0)   # .get() returns 0 if key doesn't exist
     count_in_2 = count2.get(word, 0)
 
     print(f"  Word: '{word}'")
     print(f" essay1: {count_in_1} time(s)")
     print(f" essay2: {count_in_2} time(s)")
     return True
            
  
