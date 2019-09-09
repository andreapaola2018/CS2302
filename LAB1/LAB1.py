"""
CS 2302 - Data Structures 
Andrea Ulloa
Lab 1 - Recursion 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 9/8/19
Purpose: Using recursive functions to generate anagrams of a word 
 
"""

#importing time function to time the execution of the program 
import time 

def main():
    
    #Asking the user for a word 
    global word 
    word = input("Enter a word:\n") 
    
    #Timing the execution as soon as the file is read 
    start = time.time()
    #Reading the text file 
    reading_file()

    #Checking if the word is in the word set 
    #and sending it to scramble for permutations to be made 
    if word in word_set: 
       scramble(word,'')  
        
    else: 
        print("Word does not exist")
    
    print("The word", word, "has", len(anagram_set), "anagrams:", sorted(anagram_set))   
    end = time.time()
    print("It took", end-start, "seconds to find the anagrams")

#Reading the text file and placing the words 
#into a set 
def reading_file(): 

    global word_set
    word_set = set([]) 
    global anagram_set 
    anagram_set = set([])
    global prefix_set 
    prefix_set = set([])

    global characters 
    characters = []
    
    #Reading the text file
    with open("words_alpha.txt", "r") as file:
        
        for line in file:
            
            line.strip() #Strippin whitespace 
            current_word = line[:-1]
            
            #Creating a word set of every word 
            word_set.add(current_word) 
            
            #Creating a set of prefixes for all words 
            prefix_set_build(current_word) 
     
    file.close() 
 
#Building each prefix 
def prefix_set_build(word):

    prefix = ''
    #Iterating through each word 
    for i in range(len(word)-1):
        
        temp_prefix = word[i] #Saving each character
        prefix = prefix + temp_prefix #adding previous + next character
        prefix_set.add(prefix) #Adding to the prefix set
  

def scramble(remaining, scramble1):
    prefix = ''
    
    for i in range(len(remaining)): 
       
        #Letter at index i is scrambled
        scramble_letter = remaining[i] 
        
         
        #Adding all characters to a list 
        characters.append(scramble_letter) 
        
         
        #checking for duplicate letters 
        #Stopping recursion if there are duplicate letters
        #if duplicate_check(scramble_letter) == False:
        is_duplicate = duplicate_check(scramble_letter)
            
        #Removing letter to scramble the remaining letters 
        remaining_letters = remaining[:i] + remaining[i+1:]
        #Saving every prefix 
        prefix = scramble1 + scramble_letter 
        
        #Checking that the prefix exists, and that there are no duplicate characters 
        if prefix in prefix_set and not is_duplicate:
            #scramble letter 
            scramble(remaining_letters, prefix)
            
        #Completed word, possible anagram 
        if prefix in word_set and len(remaining_letters) == 0:
            setsAnagram(prefix)              
          
#Setting anagram and making sure the original word does not get printed   
def setsAnagram(addAnagram):
   if addAnagram != word:
       anagram_set.add(addAnagram)

#Checking for duplicate characters 
def duplicate_check(character):
    
    #Checking if the character exists in the list 
    if character in characters: 
        return False #dont continue recursion if there are duplicates
    else: 
        return True
   
if __name__ == "__main__":  
   
    main()