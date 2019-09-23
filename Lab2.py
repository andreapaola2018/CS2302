"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 2 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 9/22/19
Purpose: Sorting a list to find the smallest element 

"""

#importing time function to time the execution of the program 
import time 
#Bubble sort 
def select_bubble(L,k):
    
    length = len(L)
    
    for i in range(length):
        
        for j in range(0, length-i-1):
                
            if L[j] > L[j+1]: 
                L[j], L[j+1] = L[j+1], L[j] 
     
    return L[k-1]
    
#quicksort 
def partition(L,low,high): 
    
    #index of smallest element 
    i = (low-1) 
    
    #Choosing the last element as the pivot 
    pivot = L[high]      
   
    for j in range(low , high): 
  
        #Checking that the element is less than or equal to pivot 
        if   L[j] <= pivot: 
            #incrementing index of smallest element 
            i = i+1 
            L[i],L[j] = L[j],L[i] 
    #swapping the pivot value  
    L[i+1],L[high] = L[high],L[i+1] 
    
    return (i+1)  

def quicksort(L,low,high): 
     
    #making a partition only if the low index is less than the high 
    if low < high:    
        #partitioning 
        p = partition(L,low,high) 
        #sorting first half of list, everything less than pivot
        quicksort(L,low,p-1)  
        #sorting second half of list, everything from pivot to the end 
        quicksort(L,p+1,high)   
    

def select_quick(L,k):
    length = len(L)
    #sorting the array 
    quicksort(L,0,length-1)  
    #returning 1st element if k is 0 
    if k == 0:
        return L[0]
    else:
        return L[k-1] 

#Quicksort with only one recursive call     
def select_modified_quick(L,low,high,k): 
     
    #making a partition only if the low index is less than the high 
    if low < high:    
        #partitioning arry
        p = partition(L,low,high) 
        #returning the kth element 
        if k == 0:
            select_modified_quick(L,low,p-1,k)
            
            return L[0] 
        
        elif k == p: #if kth element is the pivot 
            
            return L[k-1]
        
        elif k < p: #if k is less than the pivot 
            
            select_modified_quick(L,low,p-1,k)  
            return L[k-1]
     
        elif k > p: #k is greater than the pivot 
            select_modified_quick(L,p+1,high,k)   
            return L[k-1] 

#checking if the stack is empty 
def is_empty(stack):
    if len(stack) == 0: 
        return True
    else:
        return False 
#returning the top value of the stack 
def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]
       
#Implementing quicksort with a stack and without recursion  
def stack_quicksort(L,low,high,k):  
    ordered_stack = [] 
    temp_stack = [] 
    
    if low < high:
        
        p = partition(L,low,high)
        
        #push first half of elements of L into stack
        for i in range(0,len(L)):
            #push first half of elements of L into stack 
            temp_stack.append(L[i]) 
        
    while is_empty(temp_stack) == False:
        #popping top value of original stack 
        temp_top = peek(temp_stack) 
        
        temp_stack.pop() 
        
        #loop through values when ordered stack value is greater than peek of original stack(temp_stack)
        while is_empty(ordered_stack) == False and peek(ordered_stack) > (temp_top): 
              
            #peek from input stack then append to temp stack 
            #then pop from input stack 
            z = peek(ordered_stack)
            temp_stack.append(z)
            ordered_stack.pop()
  
        #append temp value into ordered stack  
        ordered_stack.append(temp_top)
    
    return ordered_stack[k-1]

#iterative quicksort      
def select_modified_quick2(L,low,high,k):  
     
    #making a partition only if the low index is less than the high 
    if low < high:    
        #partitioning arry
        p = partition(L,low,high) 
        n = len(L)-1
        
        #sorting the list 
        for i in range(0,n):
            #if current element is greater than next element, then swap 
            while L[i]>L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
          
    #if k is 0, then return the first element                                 
    if k == 0:
        
        return L[0] 
    
    elif k == p: #if kth element is the pivot 
        
        return L[k-1]
    
    elif k < p: #if k is less than the pivot 
         
        return L[k-1]
 
    elif k > p: #k is greater than the pivot 
       
        return L[k-1]  

#Asking the user for a list of numbers 
numbers = input("Enter numbers seperated by a space:")
#stripping the list by spaces 
num_list = list(map(int,numbers.strip().split()))

length = len(num_list)
#asking the user for the kth element 
kth_element = int(input("Enter k:\n "))

#timing the execution 
start = time.time()
#Bubble sort
print("select_bubble:", select_bubble(num_list,kth_element))
end = time.time()
print("It took", end-start, "seconds with bubble sort\n")

#quicksort
start = time.time()
print("select_quick:",select_quick(num_list,kth_element))
end = time.time()
print("It took", end-start, "seconds with quicksort\n")

#modified quicksort 
start = time.time()
print("select_modified_quick:",select_modified_quick(num_list,0,length-1,kth_element))
end = time.time()
print("It took", end-start, "seconds with modified quicksort\n")

#modified quicksort with only one while loop 
start = time.time()
print("select_modified_quick2:",select_modified_quick2(num_list,0,length-1,kth_element))
end = time.time()
print("It took", end-start, "seconds with quicksort with only one while loop\n")

#quicksort implemented with a stack 
start = time.time()
print("stack_quicksort:",stack_quicksort(num_list,0,length-1,kth_element))
end = time.time()
print("It took", end-start, "seconds with quicksort implemented with stacks\n")
