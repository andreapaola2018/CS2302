"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 7 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 12/9/19
Purpose: Implement Algorithm design techniques 
to solve the Hamiltonian Cycle problem

"""

import random
import graph_AL as graph
import graph_EL as EL
import dsf as dsf
import numpy as np


#in-degrees of each vertex in a graph
def in_degree(adjList,v):
    inEdges = 0
    for i in range(len(adjList.al)):
        for edge in adjList.al[i]:
            if edge.dest == v: 
                inEdges+=1
      
    return inEdges

#finds connected components of a graph 
def connected_components(g): 
    
    vertices = len(g.al) 
    components = vertices 
    s = dsf.DSF(vertices) 
    for v in range(vertices): 
        for edge in g.al[v]: 
            components -= s.union(v,edge.dest) 
    return components

#*****RANDOMIZATION*******
          
def randomizedHamiltonian(E,max_trials):
    
    #converting the adjacency list to edge list 
    edgeList = E.as_EL() 
    
    for i in range(max_trials):
        
        #getting random edges from the edge list 
        Eh = random.sample(edgeList.el, len(E.al))
        
        adj_list = graph.Graph(len(E.al),weighted =E.weighted, directed = E.directed)
        
        #creating adjacency list from the random list of edges
        for i in range(len(Eh)):
            
            adj_list.insert_edge(Eh[i].source,Eh[i].dest)

        
        #checking if there is one connected component 
        if connected_components(adj_list) == 1: 
            
            #iterating through the list to check if at 
            #any point a vertex in degrees is not 2
            #making it not have a hamiltonian cycle
            for i in range(len(adj_list.al)):
                
                if in_degree(adj_list,i) != 2:
                    
                    return False #not a hamiltonian cycle
            return True #is a hamiltonian cycle 

def randomization(graph,max_trials):

    for i in range(100):

        if randomizedHamiltonian(graph, max_trials)==True: 

            return True

    return False   
 
#*****BACKTRACKING*******
def backtracking(V):
    
    #making V into an edge list 
    Eh = V.as_EL()

    if len(Eh.el) == Eh.vertices:
        
        adj_list = V.as_AL()
        
        #checking if there is one connected component 
        if connected_components(adj_list) == 1: 
            
            #iterating through the list to check if at 
            #any point a vertex in degrees is not 2
            #making it not have a hamiltonian cycle
            for i in range(len(adj_list.al)):
                
                if in_degree(adj_list,i) != 2:
                    
                    return False #not a hamiltonian cycle
            return True #is a hamiltonian cycle 
        
        
    
#*****DYNAMIC PROGRAMMING*******

#a modified version of edit distance tha allows
#replacmenets only in the case where the characters 
#being interchanged are both vowels or both consonants
        
def edit_distance(s1,s2):
    #creating a list of vowels to aid in checking 
    #if the two characters are within this set or not 
    vowels = ['a','e','i','e','o','u']
    
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                d[i,j] =d[i-1,j-1]
                
            #Allowing replacements only when the characters 
            #are both vowels or both consonants
            else:
                
                if(s1[i-1] in vowels and s2[j-1] in vowels) or (s1[i-1] not in vowels and s2[j-1] not in vowels): 
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1  
                
                else: 
                     n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                     d[i,j] = min(n)+1  
    return d[-1,-1]

if __name__ == "__main__":   
    
    while True: 
        
        print("1. Randomization")
        print("2. Backtracking")
        print("3. Dynamic programming")
        
        menu = int(input("Choose an algorithm design technique\n"))
        print()
        
        if menu == 1: 
            
            #Randomization 
            g = graph.Graph(9)
            g.insert_edge(0,2)
            g.insert_edge(0,4)
            g.insert_edge(3,6)
            g.insert_edge(1,8)
            g.insert_edge(4,5)
            g.draw()
            
            print("Has a Hamiltonian Cycle: ",randomization(g,100))
            
            g2 = graph.Graph(5)
            g2.insert_edge(0,1)
            g2.insert_edge(1,2)
            g2.insert_edge(2,3)
            g2.insert_edge(3,4)
            g2.insert_edge(4,0)
            g2.draw()
            
            print("Has a Hamiltonian Cycle:",randomization(g2,100))
    
        if menu == 2:
            #has a hamiltonian cycle
            g = graph.Graph(9)
            g.insert_edge(0,2)
            g.insert_edge(0,4)
            g.insert_edge(3,6)
            g.insert_edge(1,8)
            g.insert_edge(4,5)
            g.draw()
            
            print("Has a Hamiltonian Cycle: ",backtracking(g))
            
            #no hamiltonian cycle 
            g2 = graph.Graph(5)
            g2.insert_edge(0,1)
            g2.insert_edge(1,2)
            g2.insert_edge(2,3)
            g2.insert_edge(3,4)
            g2.insert_edge(4,0)
            g2.draw()
            
            print("Has a Hamiltonian Cycle:",backtracking(g2))
            
        if menu == 3:
            
            #asking the user for two words  
            word1 = str(input("Enter the first word"))
            word2 = str(input("Enter the second word"))
            
            print("Edit Distance",edit_distance(word1,word2))
        