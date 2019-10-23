"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 2 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 10/23/19
Purpose: Comparing word embeddings to find the similarity between 
two words 

"""
import numpy as np 
import time  
#*****************B-Tree class***********************
class BTree(object):
    # Constructor
    def __init__(self,data,child=[],isLeaf=True,max_data=5):  
        self.data = data
        self.child = child 
        self.isLeaf = isLeaf
        if max_data <3: #max_data must be odd and greater or equal to 3
            max_data = 3
        if max_data%2 == 0: #max_data must be odd and greater or equal to 3
            max_data +=1
        self.max_data = max_data
    
def FindChild(T,k):
    
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree   
    for i in range(len(T.data)):
        
        if k.word < T.data[i].word:
            return i
    return len(T.data)

def Split(T):
   #splits tree by middle element when node is full 
    mid = T.max_data//2
    if T.isLeaf:
        leftChild = BTree(T.data[:mid],max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],max_data=T.max_data) 
    else:
        leftChild = BTree(T.data[:mid],T.child[:mid+1],T.isLeaf,max_data=T.max_data) 
        rightChild = BTree(T.data[mid+1:],T.child[mid+1:],T.isLeaf,max_data=T.max_data) 
    return T.data[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    
    #appends data to node 
    T.data.append(i) 
    
    #sorting in alphabetical order 
    T.data.sort(key = lambda x: x.word) 

#checks if tree is full     
def IsFull(T):
    return len(T.data) >= T.max_data

def InsertInternal(T,word_object):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,word_object)
    else:
        k = FindChild(T,word_object)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.data.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,word_object)  
        InsertInternal(T.child[k],word_object)   
 
#inserts object into B-tree 
def Insert(T,i):
     
    #if node is not full, insert internally 
    if not IsFull(T):
        InsertInternal(T,i)
    #if node is full, split the node and create a new node with 
    #the item that was split 
    else:
        m, l, r = Split(T)
        T.data =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i) 

def PrintD(T,space):
    # Prints data and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
           
    else:
        PrintD(T.child[len(T.data)],space+'   ')  
        for i in range(len(T.data)-1,-1,-1):
            print(space,T.data[i].word)
            PrintD(T.child[i],space+'   ')
            
#returns number of items stored in B-tree
def NumItems(T):
    
    #getting the length of the list of integers 
    sum = len(T.data)
    #iterating through each node of each child 
    for i in T.child:
        sum+=NumItems(i)
        
    return sum 

def Search(T,k): 
    
    # Returns node where k is, or None if k is not in the tree
    for i in range(len(T.data)):
        
        if k.word == T.data[i].word:
           
            return T.data[i]
    if T.isLeaf: 
        return None
    
    return Search(T.child[FindChild(T,k)],k) 
            
    

#height of B-tree
def Height(T):
    #once a leaf is found return 0 
    if T.isLeaf:
        return 0
    #if not add 1 to the height 
    return 1 + Height(T.child[0])    


#*****************Binary Search Tree class***********************  
class BST(object):
    def __init__(self, data, left=None, right=None):  
        self.data = data
        self.left = left 
        self.right = right  

#inserts new item into binary tree
def InsertBinary(T,newItem):
   
    if T == None:
        
        T =  BST(newItem)
    #inserting on the left or right depending on alphabetical order 
    elif T.data.word > newItem.word: 
        
        T.left = InsertBinary(T.left,newItem)
    else:
        T.right = InsertBinary(T.right,newItem)
    return T

#height of tree
def height(T): 
    
    #if tree is empty return -1 
    if T == None:
        return -1
    #check all right and left nodes 
    lh = height(T.left)
    rh = height(T.right)
    
    return 1 + max([lh,rh]) #add 1 to the max

#number of items in Binary tree 
def items(T):
    
    if T == None:
        return 0 
     
    leftNum = items(T.left)
    rightNum = items(T.right) 
    
    return 1 + sum([leftNum,rightNum])

#searching for a word in the Binary tree 
def SearchBST(T,k): 
    
    #if node is none or key is found
    
    if T == None or T.data.word == k: 
        return T 
    
    #if k comes before the current word , search left side of tree
    elif k < T.data.word:
        return SearchBST(T.left,k)
    
    #if k comes after the current word, search right side of tree
    else: 
        return SearchBST(T.right,k)
       

class WordEmbedding(object): 
    def __init__(self,word,embedding=[]): 
        # word must be a string, embedding can be a list or and array of ints or floats 
        self.word = word 
        self.emb = np.array(embedding, dtype=np.float32) 
        # For Lab 4, len(embedding=50)

if __name__ == "__main__":    
    
#Prompting the user to choose between two 
#different tree implementations  
 
    while True: 
        print("1. B-Tree Implementation")
        print("2. Binary Tree Implementation")
        
        menu = int(input("Choose a tree implementation\n"))
        print()
        
        #*****************B-Tree implementation***************** 
        if menu == 1:
            
            #ask user for max data of the B-tree  
            user_max_data = int(input("Enter max data:\n "))
            
            #creating the B-tree based of the max_data 
            T = BTree([], max_data = user_max_data)
            
            #Reading text file with words and their embeddings 
            with open("glove.6B.50d.txt", 'r', encoding='utf-8') as file: 
             
                #timing the building of the b-tree 
                start = time.time()
                    
                for line in file: 
                    #creating a list for every line 
                    list1 = line.split(" ")
                        
                    #creating a word embedding object 
                    word_object = WordEmbedding(list1[0],list1[1:])
                    
                    #inserting object into B-tree 
                    Insert(T,word_object)
                    
            end = time.time()
            print("Running time for construction of B-Tree", end-start)
            print("Height:", Height(T))
            print("Number of Items",NumItems(T),"\n") 
           
            #Reading word file to determine similarities
            
            with open("wordpairs.txt","r") as file2:
                
                #Timing the computing of the similarities 
                start2 = time.time()
                for line in file2: 
                    
                    line = line.strip().split(" ")
        
                    #searching for each word in B-tree 
                    obj1 = WordEmbedding(line[0]) #creating an object with the current word
                    obj2 = WordEmbedding(line[1])  
                    
                    word1 = Search(T,obj1) #searching for the first word 
                    word2 = Search(T,obj2) #searching for second word
                    
                    #computing similarity between the pairs of words 
                    #by using cosine distance
                    cosine_distance = np.dot(word1.emb,word2.emb)/(abs(np.linalg.norm(word1.emb))*abs(np.linalg.norm(word2.emb))) 
                    
                    print("Similarity [", word1.word, word2.word, "] =",cosine_distance)
    
            end2 = time.time()
            print("\nTime taken to compute similarities", end2-start2,"\n") 


        #*************Binary implementation******************** 
        if menu == 2: 
            #creating empty binary search tree 
            BinaryST = None 
            
            #Reading text file with words and their embeddings 
            with open("glove.6B.50d.txt", 'r', encoding='utf-8') as file: 
            #with open("embeddingtest.txt",'r') as file: 
                #timing the building of the binary tree 
                start = time.time()
                
                for line in file: 
                    #creating a list for every line 
                    binary_list = line.split(" ")
                    
                    #creating a word embedding object 
                    word_object = WordEmbedding(binary_list[0],binary_list[1:])
                    
                    #inserting object into binary tree 
                    BinaryST = InsertBinary(BinaryST,word_object)
                    
            end = time.time()
            print("Running time for construction of Binary Tree", end-start)
            print("Height:", height(BinaryST))
            print("Number of Items",items(BinaryST),"\n")
            
            
            #Reading word file to determine similarities
            
            with open("wordpairs.txt","r") as file2: 
                #Timing the computing of the similarities 
                start2 = time.time()
                
                for line2 in file2: 
                    #splitting each line and saving each item to a list 
                    listBST = line2.split(" ") 
                    
                    #stripping extra space from second word S
                    listBST[1]=listBST[1].strip()
                    
                    #searching for each word in B-tree
                    #word1, and word 2 are the nodes where the words are 
                     
                    word1 = SearchBST(BinaryST,listBST[0]) #searching for the first word 
                    word2 = SearchBST(BinaryST,listBST[1]) #searching for second word 
                    
                    #computing similarity between the pairs of words 
                    #by using cosine distance
                    cosine_distance = np.dot(word1.data.emb,word2.data.emb)/(abs(np.linalg.norm(word1.data.emb))*abs(np.linalg.norm(word2.data.emb))) 
                    
                    print("Similarity [", word1.data.word, word2.data.word, "] =",cosine_distance)
         
                    
            end2 = time.time()
            print("\nTime taken to compute similarities", end2-start2,"\n") 
                   