# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge2:
    def __init__(self, dest, weight=1):
     
        self.dest = dest
        self.weight = weight
class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
    
    #inserts edge into edge list 
    def insert_edge(self,source,dest,weight=1):
        #checks if the value of any attribute is out of range 
        if source <0 or dest<0:
            print('Error, vertex number out of range')
            
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        
        else:
            self.el.append(Edge(source,dest,weight))
         
    
    def delete_edge_(self,source,dest):
             
        i = 0
        #going through each edge in the list 
        for edge in self.el:
            #deleting by comparing the source and dest 
            if edge.source == source and edge.dest == dest:
                self.el.pop(i)
                return True
                    
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        
        if source <0 or dest<0:
            print('Error, vertex number out of range')
        
        else:
            deleted = self.delete_edge_(source,dest)
            
        if not deleted:        
            print('Error, edge to delete not found')     
        
                
    def display(self):
      print('[',end='')
      
      for edge in self.el:
          
          print('('+str(edge.source)+','+str(edge.dest)+','+str(edge.weight)+')',end='')
          
      print(']') 
     
    def draw(self):
        
        adj_list = self.as_AL()
        
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(adj_list)):
            for edge in adj_list[i]:
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
       
    #returns edge list 
    def as_EL(self):
        return self
    
    #returns adjacency matrix 
    def as_AM(self):
        
       #creating empty matrix 
       AM = np.zeros((self.vertices,self.vertices),dtype=int)-1 
       
       #iterating through edge list 
       for edge in self.el:
           
           source, dest, weight = edge.source, edge.dest, edge.weight
           #add source, dest and weight to adjacency matrix 
           AM[source][dest] = weight
        
       return AM
    
    def as_AL(self):
        #creating empty list 
        AL = [[] for i in range(self.vertices)]
        
        for edge in self.el:
            
            source, dest, weight = edge.source, edge.dest, edge.weight
            
            AL[source].append(Edge2(dest, weight))
            
        return AL 
    
    def bfs(self,start,end): 
        #queue
        queue = [start]

        discoveredSet = [start]

        path = [-1] * 16
        #while queue is not emptpy pop first element 
        while queue:

            vertex = queue.pop(0)

            for edge in self.el:
                #if at correct vertex and the destination has not been visited
                if edge.source == vertex and edge.dest not in discoveredSet:

                    queue.append(edge.dest)

                    discoveredSet.append(edge.dest)

                    path[edge.dest] = edge.source 

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
            for edge in self.el: 
                if edge.source == vertex: 
                    stack.append(edge.dest)
                    
        return path
    
    def printPathD(self, path, dest):

        for i in range(len(path)):
            
            print(path[i], end = " ")
            
            if path[i] == dest:
                break
    
    def printPathB(self, path, dest):

        if path[dest] != -1:

            self.printPathB(path, path[dest])

            print(dest, end = " ")

        else:

            print(dest, end = " ")

            return -1
        
    def outDegree(self,v):
        counter = 0 
        for edge in self.el: 
            
            if edge.source == v:
                counter+=1
        return counter 


                