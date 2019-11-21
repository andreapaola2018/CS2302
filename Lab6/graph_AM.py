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
        
        adjList = self.as_AL()
        
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(adjList)):
            for edge in adjList[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=15,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
    
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
        
        adjacency_list =  [[] for i in range(len(self.am))]
        
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                
                if self.am[i][j] != -1:
                    
                    adjacency_list[i].append(Edge(self.am[j],self.am[i][j]))
                    
        return adjacency_list

     #breadth-first search 
    def bfs(self, initial): 
    
        #marking all vertices as not visited  
        visited = [False] * (len(self.al)) 
       
        queue = [] 
      
        queue.append(initial) 
        visited[initial] = True
      
        while queue: 
      
            #dequeue vertex from queue then print 
            initial = queue.pop(0)
            
            print (initial, end = " ") 
      
            #Get all adjacent vertices of the 
            #dequeued vertex
            #If a adjacent vertex has not been visited, then mark it 
            #visited and enqueue it 
            for edge in self.al[initial]: 
                    
                if visited[edge.dest] == False: 
                    
                    queue.append(edge.dest) 
                    visited[edge.dest] = True
                    
                    
graph = Graph(16)

graph.insert_edge(0, 5)
graph.insert_edge(2, 11)
graph.insert_edge(2, 7)
graph.insert_edge(4, 5)
graph.insert_edge(4, 7)
graph.insert_edge(4, 13)
graph.insert_edge(8, 11)
graph.insert_edge(8, 13)
graph.insert_edge(10, 11)
graph.insert_edge(10, 15) 
graph.draw() 