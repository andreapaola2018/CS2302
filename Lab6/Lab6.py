"""
CS 2302 - Data Structures 
Andrea Ulloa 
Lab 6 
Professor: Olac Fuentes 
TA: Anindita Nath 
Date of last modification: 11/18/19
Purpose: Using graphs to find a solution to a problem using 
a search algorithm 
"""
import graph_AM as AM 
import graph_EL as EL
import graph_AL as AL 

        
def bfs(graph, initial): 
    
    # Mark all the vertices as not visited 
    visited = [False] * (len(graph.al)) 
  
    #queue for BFS 
    queue = [] 
  
    queue.append(initial) 
    visited[initial] = True
  
    while queue: 
  
        # Dequeue a vertex from  
        # queue and print it 
        initial = queue.pop(0) 
        print (initial, end = " ") 
  
        # Get all adjacent vertices of the 
        # dequeued vertex s. If a adjacent 
        # has not been visited, then mark it 
        # visited and enqueue it 
        for edge in graph.al[initial]: 
                
            if visited[edge.dest] == False: 
                
                queue.append(edge.dest) 
                visited[edge.dest] = True
#depth first search 
def dfs(graph,start):
    
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
        for edge in graph.al[vertex]: 
            
            stack.append(edge.dest)
                
    return path

 
if __name__ == "__main__":
    
    
    while True:
        
        print("1. Part 1")
        print("2. Part 2")
        
        choice = int(input("Choose a part of the program\n"))
        print()
        
        if choice == 1:
            
            adjList = AL.Graph(16)
            adjMatrix = AM.Graph(16)
            edgeList = EL.Graph(16)
            
            print()    
        
        if choice == 2:    
            #asking the user to choose a graph representation
            while True: 
                
                print("1. Adjacency List")
                print("2. Adjacency Matrix")
                print("3. Edge List")
                
                menu = int(input("Choose a graph representation\n"))
                print()
                
                
                if menu == 1:
                    #creating adjacency list with 16 vertices 
                    graph = AL.Graph(16) 
                    adj_list = graph.asAL()
                    
                    
                if menu == 2:
                    #creating adjacency matrix with 16 vertices 
                    graph = AM.Graph(16) 
                    adj_list = graph.as_AL()
                    
                if menu == 3:
                    
                    #creating edge list with 16 vertices 
                    graph = EL.Graph(16) 
                    adj_list = graph.as_AL() 
                    
                
                #inserting edges
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
                 
                while True: 
                
                    print("1. Breadth-First Search")
                    print("2. Depth-First Search")
                    
                    menu = int(input("Choose a search algorithm\n"))
                    print()
                    
                    if menu == 1:
                        print("Breadth-First Search",bfs(graph,0))
                    
                    if menu == 2: 
                        print("Depth-First Search",dfs(graph,0))
                