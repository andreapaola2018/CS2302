# Adjacency list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

import dsf as dsf
import graph_EL as EL      
class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')      
            
    def display(self):
        
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
        
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
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
        
    
    #returns edge list representation         
    def as_EL(self):
        #creating empty edge list 
        edge_list = EL.Graph(len(self.al))
        
        #iterating through edge list 
        for i in range(len(self.al)):
            
            for edge in self.al[i]:
                
                edge_list.insert_edge(i,edge.dest,edge.weight)
        
        return edge_list
                        
    #returns adjacency matrix representation
    
    def as_AM(self):
        
        matrix = AM.Graph(len(self.al)) 
        
        for i in range(len(self.al)):
            for edge in self.al[i]:

                matrix.insert_edge(i,edge.dest)
            
        return matrix 
    
    
    #returns adjacency list representation
    def as_AL(self):
        return self
    
    def bfs(self,initial): 
        
        # Mark all the vertices as not visited 
        visited = [self.al[initial]] 
      
        #queue for BFS 
        queue = [self.al[initial]]
        
        path = [-1] *16
      
        while queue: 
      
            #Dequeue a vertex from  
            #queue 
            vertex = queue.pop(0) 
      
            for edge in vertex:
                
                if self.al[edge.dest] not in visited:
                    
                    queue.append(self.al[edge.dest])
                    visited.append(self.al[edge.dest])
                    path[edge.dest] = self.al.index(vertex)
                
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
            for edge in self.al[vertex]: 
                
                stack.append(edge.dest)
                    
        return path
    
    def printPath(self, path, dest):

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
    
    #removes all edges going out from v 
    def removes(self,v):
        i = 0 
        for edge in self.al[v]:
            
            self.al[v].pop(i)
            i+=1
    
    def nearestNeighbor(self,v):
        nn = -1
        min_w = math.inf
        for edge in self.al[v]:
            if edge.weight < min_w:
                min_w = edge.weight 
                nn = edge.dest
        return nn
    
     #finds connected components of a graph 
    def connected_components(self): 
        
        vertices = len(self.al) 
        components = vertices 
        s = dsf.DSF(vertices) 
        for v in range(vertices): 
            for edge in self.al[v]: 
                components -= s.union(v,edge.dest) 
        return components, s
            