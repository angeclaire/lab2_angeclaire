## PLAGIARISM DETECTOR APPLICATION

# What my script does

When you run the script, it will automatically load two essays named essay1.txt and essay2.txt from the same folder .It will clean and process the text from both files by converting all words to lowercase and removing punctuation, then count how many times each word appears in each essay .You will then be presented with an interactive menu where you can choose to view common words between the two essays, search for specific word, or calculate the plagiarism percentage. before running the script ensure that both essay1.txt and essay2.txt are placed in the same folder as plagiarism_detector_application.py .

"""
Project structure
lab2_angeclaire/
├── plagiarism_detector_application.py
├── essay1.txt
├── essay2.txt
└── README.md

"""

# Menu option

Once the essays are loaded you will see a menu with four choices. Type 1 to
display all words that appear in both essays along with how many times each word
appears in each essay. Type 2 to search for a specific word and see how often
it appears in Essay 1 and Essay 2. The program will return True if the word is
found in at least one essay and False if it is not found in either. Type 3
to calculate the plagiarism percentage using the formula below. Type 4 to exit
the program.


# How the plagiarism percentage is calculated

the program uses set opeartions to compare the essays .it finds the intersection which are the words that appear in both essays, and the union which are all unique words from both essays combined 

Plagiarism % = (Intersection / Union) × 100

If the result is 50% or more the program will print that plagiarism has been
detected. If the result is below 50% the program will print that no plagiarism
has been detected.

