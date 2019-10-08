"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 2 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 10/6/19
Purpose: Perform various operations on a linked list
while making sure the list is sorted in ascending order  

"""
import time
import math 
import random
#Constructor
class Node(object):
    
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 

class SortedList(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
        
    #prints content of the list in ascending order
    def Print(self):
            t = self.head
            while t is not None:
                   print(t.data,end=' ')
                   t = t.next
            print() 
    def Append(self,x):
         
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            
    def AppendList(self,python_list):
        
        for d in python_list:
            self.Append(d)
    
    #Inserts integer i to the list 
    def Insert(self,i): 
        
        #Creating a head if the list is empty 
        if self.head is None:
            self.head = Node(i) 
            self.tail = self.head 
            return
        
        #Adding a node to a list that contains only a head node
        #comparing head data to i 
        if self.head.data >= i: 
            #Creating new node 
            new_node = Node(i) 
            #setting the next of the node to the head
            new_node.next = self.head 
            #Assigning the head to the new node 
            self.head = new_node
            return 
        
        else:
            #checking the node next to current and comparing the data to i 
            current = self.head
            
            #iterating through list until node of greater value is found 
            while (current.next is not None and current.next.data < i): 
                
                #iterating to next node if i is less than the nodes data  
                current = current.next
            #inserting if the current node is larger than i         
            new = Node(i)
            new.next = current.next
            current.next = new
        
    #Deleting a specified node in the list 
    def Delete(self,i):
        
        #Checking if list is empty 
        if self.head is None:
            return 
        
        t = self.head 
        #removing head node and reassigning head pointer 
        if self.head.data == i: 
            self.head = self.head.next
            #Setting old head to none 
            t = None
            return
        
        while t is not None:
            #Setting new pointers 
            if t.next.data == i:
                t.next = t.next.next 
                #Setting new tail when tail 
                #node needs to be removed 
                if self.tail.data == i:
                    
                    self.tail = t 
              
                return  
            t = t.next 
            #If item does not exist in list 
            if t.next is None:
                print(i,"does not exist")
                return
    
    #merging linked lists         
    def Merge(self,M):
        
        #iterating through M list 
        current = self.head
        
        while current is not None:
            #inserting each element of M 
            L.Insert(current.data)
            current = current.next 
            
    #Returns index of i  
    def IndexOf(self,i):
        t = self.head 
        #counter for the indices
        count = 0
        while t is not None:
            #if the data is equivalent return the counter 
            if t.data == i:
                
                return count
            count+=1
            t = t.next 
            
        return -1
    
    def Clear(self): 
        #iterating through M list 
        current = self.head
        while current is not None:
            #inserting each element of M 
            L.Delete(current.data)
            current = current.next 
        
    
    #Returns smallest element in the list 
    def Min(self):
        if self.head is None and self.tail is None:
            print("list is empty") 
            
        #checking if list is empty 
        if self.head is None and self.tail is None:
            return math.inf 
        else: 
            return self.head.data 
    
    #Returns largest element in the list 
    def Max(self):
        
        #checking if list is empty 
        if self.head is None and self.tail is None:
            return -math.inf 
        else: 
            return self.tail.data     
    
    #Returns true if the list has duplicate elements     
    def HasDuplicates(self): 
       t = self.head 
       
       while t.next is not None: 
           #comparing current node to the next node 
           #returning true if the data matches 
           if t.data == t.next.data:
               return True 
           t = t.next 
       return False
    
    #returning kth element 
    def Select(self,k):
        
        t = self.head 
        #iterating to the kth element 
        for i in range(k):
            
            t = t.next 
        #returning the data of the kth element     
        return t.data 
            
            
               
#Normal List class     
class List(object):   
    # Constructor
    def __init__(self,head = None,tail = None):    
        self.head = head
        self.tail = tail
        
    #prints content of the list in ascending order
    def Print(self):
            t = self.head
            while t is not None:
                   print(t.data,end=' ')
                   t = t.next
            print() 
    
    def Append(self,x):
         
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
            
    def AppendList(self,python_list):
        for d in python_list:
            self.Append(d)
            
     #Inserts integer i to the list 
    def Insert(self,i): 
        
        #Creating a head if the list is empty 
        if self.head is None:
            self.head = Node(i) 
            self.tail = self.head 
            return
        
        #Adding a node to a list that contains only a head node
        #comparing head data to i 
        if self.head.data >= i: 
            #Creating new node 
            new_node = Node(i) 
            #setting the next of the node to the head
            new_node.next = self.head 
            #Assigning the head to the new node 
            self.head = new_node
            return 
        
        else:
            #checking the node next to current and comparing the data to i 
            current = self.head
            
            #iterating through list until node of greater value is found 
            while (current.next is not None and current.next.data < i): 
                
                #iterating to next node if i is less than the nodes data  
                current = current.next
            #inserting if the current node is larger than i         
            new = Node(i)
            new.next = current.next
            current.next = new
            
     #Deleting a specified node in the list 
    def Delete(self,i):
        
        #Checking if list is empty 
        if self.head is None:
            return 
        
        t = self.head 
        #removing head node and reassigning head pointer 
        if self.head.data == i: 
            self.head = self.head.next
            #Setting old head to none 
            t = None
            return
        
        while t is not None:
            #Setting new pointers 
            if t.next.data == i:
                t.next = t.next.next 
                #Setting new tail when tail 
                #node needs to be removed 
                if self.tail.data == i:
                    
                    self.tail = t 
              
                return  
            t = t.next 
             #If item does not exist in list 
            if t.next is None:
                print(i,"does not exist")
                return
            
    #merging linked lists         
    def Merge(self,M):
        
        #iterating through M list 
        current = self.head
        while current is not None:
            #inserting each element of M 
            normal_list.Insert(current.data) 
            current = current.next 
            
    #Returns index of i  
    def IndexOf(self,i):
        t = self.head 
        #counter for the indices
        count = 0
        while t is not None:
            #if the data is equivalent return the counter 
            if t.data == i:
                
                return count
            count+=1
            t = t.next 
            
        return -1
    
    def Clear(self): 
        if self.head is None and self.tail is None:
            print("list is empty") 
        #iterating through M list 
        current = self.head
        while current is not None:
            #inserting each element of M 
            normal_list.Delete(current.data)
            current = current.next
            
    #Returns smallest element in the list 
    def Min(self):
        
        #checking if list is empty 
        if self.head is None and self.tail is None:
            return math.inf 
        else: 
            #setting current and min to first value 
            current = self.head
            min = current.data
            while current is not None: 
                #checking if the current is less than the min
                if current.data < min :
                    #updating min 
                    min = current.data

                current = current.next 
                
            return min
        
     #Returns largest element in the list 
    def Max(self):
        
        #checking if list is empty 
        if self.head is None and self.tail is None:
            return -math.inf 
        else: 
            #finding max 
            current = self.head
            #setting max to the head
            max = current.data
            while current is not None: 
                #checking if max is less than current 
                #if it is less, update max value 
                if max < current.data:
                    max = current.data
                current = current.next 
                
            return max          
        
    #Returns true if the list has duplicate elements     
    def HasDuplicates(self): 
       t = self.head 
       
       while t.next is not None: 
           #comparing current node to the next node 
           #returning true if the data matches 
           if t.data == t.next.data:
               return True 
           t = t.next 
       return False
   
    #returning kth element 
    def Select(self,k):
        
        t = self.head  
        #iterating till the kth element 
        for i in range(k):
            
            t = t.next 
        #returning the data of the kth node    
        return t.data 


#"""
#******SORTED LIST******
L = SortedList()
#Random generator for a list 
S = random.sample(range(0, 10), 6)

#******NORMAL LIST******
normal_list = List()
normal_list.AppendList(S)

#sorting 
S.sort()
L.AppendList(S)

#autogenerating a sorted version of the normal list 
normal_list2 = List()
normal_list2.AppendList(S)

#merged list to be merged to a sorted list  
merged1 = SortedList()
rando_list = random.sample(range(0, 10), 5)
rando_list.sort()
merged1.AppendList(rando_list)

#merged list to be merged to a regular list 
merged2 = List()
merged2.AppendList(rando_list)

#"""
#Menu for different functions 
while True: 
    print("1. Print()")
    print("2. Insert()")
    print("3. Delete()")
    print("4. Merge()")
    print("5. IndexOf()")
    print("6. Clear()")
    print("7. Min()")
    print("8. Max()")
    print("9. HasDuplicates()")
    print("10. Select()")

    menu = int(input("Choose a function\n"))
    print()
    
    #Print
    if menu == 1:
        start = time.time()
        print("Sorted List:")
        L.Print()
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        normal_list.Print() 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")  
        
    #insert   
    elif menu == 2: 
        print("***Inserting 10***")
        start = time.time()
        L.Insert(10)
        print("Sorted List:")
        L.Print()
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        normal_list.Insert(10)
        print("Normal List:")
        normal_list.Print()
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
    #delete    
    elif menu == 3: 
        print("***Deleting 10***")
        start = time.time()
        print("Sorted List:")
        L.Delete(10)
        L.Print()
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        normal_list.Delete(10)  
        normal_list.Print()
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
    #merge    
    elif menu == 4:
        start = time.time()
        print("Original Sorted list:")
        L.Print()
        print("Merged Sorted List:")
        merged1.Merge(L)
        L.Print()
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Original Normal list:")
        normal_list.Print()
        print("Merged Normal List:")
        merged2.Merge(normal_list) 
        normal_list.Print()
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
   
    #IndexOf    
    elif menu == 5:
        print("***Index of 1***")
        start = time.time()
        print("Sorted List:")
        L.Print()
        print("Index Sorted:",L.IndexOf(1))
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        normal_list.Print()
        print("Index Normal:",normal_list.IndexOf(1)) 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
        
    #Clear          
    elif menu == 6:
        start = time.time()
        print("Sorted List:")
        L.Clear()
        L.Print()
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        normal_list.Clear()  
        normal_list.Print()
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
        
    #minimum 
    elif menu == 7:
        start = time.time()
        print("Sorted List:")
        print("Minimum",L.Min())
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        print("Minimum",normal_list.Min()) 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
        
    #maximum    
    elif menu == 8:
        start = time.time()
        print("Sorted List:")
        print("Maximum:",L.Max())
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        print("Maximum:",normal_list.Max()) 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
        
    #duplicates     
    elif menu == 9:
        start = time.time()
        print("Sorted List:")
        print("Duplicates:",L.HasDuplicates())
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        print("Duplicates:",normal_list2.HasDuplicates()) 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")
        
    #kth element     
    elif menu == 10:
        start = time.time()
        print("***finding 3rd smallest element***")
        print("Sorted List:")
        L.Print()
        print("Kth element:",L.Select(3))
        endtime = time.time()
        totalTimeSorted = endtime-start
        start2 = time.time()
        print("Normal List:")
        normal_list2.Print()
        print("Kth element:",normal_list2.Select(3)) 
        endtime2 = time.time()
        totalTimeNormal = endtime2-start2 
        print("\nSorted List run time is",totalTimeSorted, "\nNormal List run time is", totalTimeNormal,"\n")