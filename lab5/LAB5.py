"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 5 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 11/4/19
Purpose: Comparing word embeddings to find the similarity between 
two words by using hash tables

"""
import numpy as np 
import time  

class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
         #creates a list where each item is an empty list
        self.bucket = [[] for i in range(size)]
        
#returns index where the string should be placed      
    def h(self,k):
        
        return len(k.word)%len(self.bucket)    
            
            
    def insert(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(k)
        if not k.word in self.bucket[b]:
            self.bucket[b].append(k) #Insert new item at the end
            
    def find(self,k):
        
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(k)
    
        try:
            #iterating through each item in the bucket
            for i in range(len(self.bucket[b])):
                if self.bucket[b][i].word == k.word:
                    return b, i 
        
        except:
            i = -1 #item is not in list 
        return b, i
    
    #number of elements in table divided by the size of the table 
    def load_factor(self):
        items = 0 
        #goes through elements within table 
        for i in self.bucket: 
            items+=len(i)
        return items/len(self.bucket) 

class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to None (which means empty)
    # Constructor
    def __init__(self,size):  
        self.item = [None for i in range(size)]
        
    def h(self,k):
        return k%len(self.item) 
        
    def insert(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)):
            pos = self.h(len(k.word)+i)
            if self.item[pos] == None:
                self.item[pos] = k
               
                return pos
        return -1
    
    def find(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h(len(k.word)+i)
            if self.item[pos].word == k.word:
                return pos
            if self.item[pos] == None:
                return -1
        return -1
    
    #number of elements in table divided by the size of the table 
    def load_factor(self):
        items = 0 
        #goes through elements within table 
        for i in range(len(self.item)): 
            if self.item[i] != None:
                items+=1
        return items/len(self.item) 

        
#length of string % n
def stringModn(word,n):
    return len(word)%n

#Ascii value of the first character in the string % n
def asciiVal1(word,n):
    
    firstChar = ord(word[0])
    
    return firstChar%n 

#product of ascii values of first and last characters 
def productAscii(word,n): 
    
    #ascii value of first character  
    first = asciiVal1(word,n)
    
    #ascii value of first character
    lastChar = ord(word[-1])
    
    product = first * lastChar
    return product%n

#sum of ascii values of all characters in the string 
def sumAscii(word,n):
    sum1 = 0 
    for i in range(len(word)): 
        sum1 += ord(word[i])
    
    return sum1%n

def h_recursive(S,n):
    if len(S) == 0:
        return 1 
    return (ord(S[0])+255*h_recursive(S[1:],n))%n


        

class WordEmbedding(object): 
    def __init__(self,word,embedding=[]): 
        # word must be a string, embedding can be a list or and array of ints or floats 
        self.word = word 
        self.emb = np.array(embedding, dtype=np.float32) 
        # For Lab 4, len(embedding=50)


if __name__ == "__main__":    
    
#Prompting the user to choose between two 
#different hash implementations
 
    while True: 
        
        print("1. Chaining")
        print("2. Linear-Probing")
        
        menu = int(input("Choose a hash table implementation\n"))
        print()
        
        #*****************Chaining***************** 
        if menu == 1:
            #Creating hash table with chaining 
            h = HashTableChain(3)
            
            #Reading text file with words and their embeddings 
            with open("glove.6B.50d.txt", 'r', encoding='utf-8') as file: 
             
                #timing the building of the hash table
                start = time.time()
                    
                for line in file: 
                    
                    #creating a list for every line 
                    list1 = line.split(" ")
                        
                    #creating a word embedding object 
                    word_object = WordEmbedding(list1[0],list1[1:])
                    
                    #inserting word embedding object into hash table 
                    h.insert(word_object)
                    
            
            end = time.time()
            print("Running time for construction of HashTableChain", end-start, "\n")
            
            #Reading word file to determine similarities
            with open("wordpairs.txt","r") as file2:
                
                #Timing the computing of the similarities 
                start2 = time.time()
                
                for line in file2: 
                    
                    #splitting and stripping each line 
                    line = line.strip().split(" ")
                    
                    #creating an object with the current word only 
                    obj1 = WordEmbedding(line[0]) 
                    obj2 = WordEmbedding(line[1])  
                    
                    #returning the bucket and index of the word 
                    y1, x1 = h.find(obj1) #searching for the first word 
                    y2, x2 = h.find(obj2) #searching for second word 
                    
                    
                    #computing similarity between the pairs of words 
                    #by using cosine distance
                    cosine_distance = np.dot(h.bucket[y1][x1].emb,h.bucket[y2][x2].emb)/(abs(np.linalg.norm(h.bucket[y1][x1].emb))*abs(np.linalg.norm(h.bucket[y2][x2].emb)))
                    print("Similarity [", h.bucket[y1][x1].word, h.bucket[y2][x2].word, "] =",cosine_distance)
    
            end2 = time.time()
            print("\nTime taken to compute similarities", end2-start2,"\n") 
            
            #extra functions     
            string = input("Type in a string")
            print()
            
            print("1. length of string % n")
            print(stringModn(string,len(h.bucket)),"\n")
            
            print("2. ascii value of first character%n")
            print(asciiVal1(string,len(h.bucket)),"\n")
            
            print("3. product of ascii values")
            print(productAscii(string,len(h.bucket)),"\n")
            
            print("4. sum of ascii values")
            print(sumAscii(string,len(h.bucket)),"\n")
            
            print("5. recursive formulation")
            print(h_recursive(string,len(h.bucket)),"\n")
            
            print("6. load factor")
            print(h.load_factor(),"\n")
                
         #*************linear-probing******************** 
        if menu == 2: 
            
            counter = 0
            #counting the number of lines in the file for the size of hash table
            with open("glove.6B.50d.txt", 'r', encoding='utf-8') as file:
            #with open("test.txt", 'r') as file:
                for line in file:
                    counter+=1
                    
            #Creating hash table with linear-probing
            h = HashTableLP(counter)
            
            #Reading text file with words and their embeddings 
            #with open("glove.6B.50d.txt", 'r', encoding='utf-8') as file: 
            with open("test.txt", 'r') as file:
                
                #timing the building of the hash table
                start = time.time()
                    
                for line in file: 
                    
                    #creating a list for every line 
                    list1 = line.split(" ")
                        
                    #creating a word embedding object 
                    word_object = WordEmbedding(list1[0],list1[1:])
                    
                    #inserting word embedding object into hash table 
                    h.insert(word_object)
        
                    
            end = time.time()
            print("Running time for construction of HashTableLP", end-start,"\n")
                    
            #Reading word file to determine similarities
            with open("wordpairs.txt","r") as file2:
                
                #Timing the computing of the similarities 
                start2 = time.time()
                
                for line in file2: 
                    
                    #splitting and stripping each line 
                    line = line.strip().split(" ")
                    
                    #creating an object with the current word only 
                    obj1 = WordEmbedding(line[0]) 
                    obj2 = WordEmbedding(line[1])  
                    
                    #returning the index of the word 
                    x1 = h.find(obj1) #searching for the first word 
                    x2 = h.find(obj2) #searching for second word 
                    
                    
                    cosine_distance = np.dot(h.item[x1].emb,h.item[x2].emb)/(abs(np.linalg.norm(h.item[x1].emb))*abs(np.linalg.norm(h.item[x2].emb)))
                    print("Similarity [", h.item[x1].word, h.item[x2].word, "] =",cosine_distance)
           
            end2 = time.time()
            
            print("\nTime taken to compute similarities", end2-start2,"\n")
            #extra functions     
            string = input("Type in a string")
            print()
            
            print("1. length of string % n")
            print(stringModn(string,len(h.item)),"\n")
            
            print("2. ascii value of first character%n")
            print(asciiVal1(string,len(h.item)),"\n")
            
            print("3. product of ascii values")
            print(productAscii(string,len(h.item)),"\n")
            
            print("4. sum of ascii values")
            print(sumAscii(string,len(h.item)),"\n")
            
            print("5. recursive formulation")
            print(h_recursive(string,len(h.item)),"\n")
            
            print("6. load factor")
            print(h.load_factor(),"\n")
