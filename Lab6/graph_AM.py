# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as AL


class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        
        if source >= len(self.am) or dest >= len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
            
        else:
            #checks if not directed 
            if not self.directed: 
                
                self.am[source][dest] = weight 
                self.am[dest][source] = weight 
                
            #else graph is directed 
            else:
                self.am[source][dest] = weight 
        
    def delete_edge(self,source,dest):
        
        if not self.directed:
            self.am[source][dest] = -1 
            self.am[dest][source] = -1 
            
        else:
            self.am[source][dest] = -1

    def display(self):
        
        for i in range(len(self.am)):
            
            for j in range(len(self.am[i])):
                
                print(self.am[i][j], end = " ")
            print()
     
    def draw(self):
        
        self.as_AL().draw() 
    
    #returns edge list representation of the graph 
    def as_EL(self): 
        
        EL = []

        for i in range(len(self.am)): 
            
            for j in range(len(self.am[i])):
                
                if self.am[i][j] != -1:
                
                    EL.append(Edge(self.am[i],self.am[j],self.am[i][j]))
                
        return EL
    
    #returns an adjacency matrix representation of the graph
    def as_AM(self):
        
        return self
    
    
    #returns an adjacency list representation of the graph 
    def as_AL(self):
        
        adjacency_list = AL.Graph(len(self.am))
        
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                
                #If not directed break out of for
                if i == j and not self.directed:
                    break
                
                #if item in matrix is 1, the add to adjacency list
                if self.am[i][j] != -1:
                    
                    adjacency_list.insert_edge(i,j,self.am[i][j])
                    
        return adjacency_list

     #breadth-first search 
    def bfs(self, initial): 
    
        #marking all vertices as not visited  
        visited = [initial] 
       
        queue = [initial] 
        
        path = [-1] * 16
      
        while queue: 
      
            #dequeue vertex from queue then print 
            vertex = queue.pop(0)
      
            #Get all adjacent vertices of the 
            #dequeued vertex
            #If a adjacent vertex has not been visited, then mark it 
            #visited and enqueue it 
            for i in range(len(self.am[vertex])):
                
                if self.am[vertex][i] != -1 and i not in visited: 
                    
                    queue.append(i) 
                    visited.append(i)
                    path[i] = vertex
        return path
    
    #depth first search 
    def dfs(self,start,end):
        
        #stack initialized with the start of the path 
        stack = [start]
        #shortest path from start to end
        path = []
        
        #while stack is not empty 
        while stack:
            
            #pop stack and set that element to the curretn vertex
            vertex = stack.pop()
            
            if vertex in path:
                continue 
            #append current vertex to the path 
            path.append(vertex) 
            
            #iterate through each edge of the vertex
            for i in range(len(self.am[vertex])): 
                if self.am[vertex][i] != -1:

                    stack.append(i)
                    
        return path
    
    
    def printPathB(self, path, dest):
    
        if path[dest] != -1:
    
            self.printPathB(path, path[dest])
    
            print(dest, end = " ")
    
        else:
    
            print(dest, end = " ")
    
            return -1
        
    def printPathD(self, path, dest):

        for i in range(len(path)):
            
            print(path[i], end = " ")
            
            if path[i] == dest:
                break