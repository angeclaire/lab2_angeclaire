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

def calculate_plagiarism(count1, count2):#this function calculates the plagiarism percantage using set operations.
     
     set1 = set(count1.keys())
     set2 = set(count2.keys())

     intersection = set1 & set2
     union = set1 | set2

     if len(union) == 0:
         print(" [WARNING] Both essays appear to be empty. Cannot calculate percentage.")       
         return 0.0
     
     plagiarism_percent = (len(intersection) / len(union)) * 100
     
     print(f"\n  Unique words in Essay 1 : {len(set1)}")
     print(f"  Unique words in Essay 2 : {len(set2)}")
     print(f"  Intersection (common): {len(intersection)}")
     print(f"  Union (total unique) : {len(union)}")
     print(f"\n  Plagiarism Percentage : {plagiarism_percent:.2f}%")

     if plagiarism_percent  >= 50:
         print("Plagiarism detected greater than 50%")
     else:
         print("plagiarism detected is less than 50%") 

     return plagiarism_percent
       
 #main program starts here
def main ():
    print("PLAGIARISM DETECTOR APPLICATION")
    print("\n[1] loading essays...")
    word1 = load_essay("essay1.txt")
    word2 = load_essay("essay2.txt")
     
    if not word1 or not word2:
        print("\n cannot proceed without both essays.exiting")
        return
        
        print(f"  essay1.txt loaded → {len(words1)} total words")
        print(f"  essay2.txt loaded → {len(words2)} total words")

        count1 = count_words(words1)
        count2 = count_words(words2)

        while True:
         print("  [1] Show common words between essays")
         print("  [2] Search for a specific word")
         print("  [3] Calculate plagiarism percentage")
         print("  [4] Exit")

         choice = input("  Enter your choice (1/2/3/4): ").strip()
 
        # Input validation: must be one of the valid options
        if choice not in ["1", "2", "3", "4"]:
            print("  [ERROR] Invalid choice. Please enter 1, 2, 3, or 4.")
            continue
            
        if choice == "1":
            print("Common Words")
            find_common_words(count1, count2)
            

        elif choice == "2":
             word = input("\n  Enter the word to search for: ")
             print("Search Result")
             result = search_word(word, count1, count2)
             
             print(f"  Found: {result}")
 
        elif choice == "3":
             print("\n Plagiarism Analysis ")
             calculate_plagiarism(count1, count2)
 
        elif choice == "4":
            print("\n  Goodbye! Thanks for using Plagiarism Detector.\n")
            break
 
  #Entry point
if __name__ == "__main__":
    main()
 
