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
import time

def graph_build():
    
    #creating adjacency list with 16 vertices 
    graph = AL.Graph(16) 
    
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
    
    matrix = graph.as_AM()
    
    edge_list = graph.as_EL()
    
    return graph, matrix, edge_list



if __name__ == "__main__":
    
        
    graph, matrix, edge_list = graph_build()
   
    
    print("*****ADJACENCY LIST******")
    start = time.time()
    print("\nBreadth-First Search Adjacency List:")
    path = graph.bfs(0)
    graph.printPathB(path,15)
    end = time.time()
    print("\nRunning time for BFS using an Adjacency List:", end-start,"\n")
    
    start = time.time()
    print("Depth-First Search Adjacency List:")
    path = graph.dfs(0,15)
    graph.printPath(path,15)
    print()
    end = time.time()
    print("Running time for DFS using an Adjacency List:", end-start,"\n")
    
    
    print("*****ADJACENCY MATRIX******")
    start = time.time()
    print("\nBreadth-First Search Adjacency Matrix:")
    path = matrix.bfs(0)
    matrix.printPathB(path,15)
    end = time.time()
    print("\nRunning time for BFS using an Adjacency Matrix:", end-start,"\n")
    
    start = time.time()
    print("\nDepth-First Search Adjacency Matrix:")
    path = matrix.dfs(0,15)
    matrix.printPathD(path,15)
    print()
    end = time.time()
    print("Running time for DFS using an Adjacency Matrix:", end-start,"\n")
    
    print("*****EDGE LIST******")
    start = time.time()
    print("\nBreadth-First Search Edge List:")
    path = edge_list.bfs(0,15)
    edge_list.printPathB(path,15)
    end = time.time()
    print("\nRunning time for BFS using an Edge List:", end-start,"\n")
    
    start = time.time()
    print("\nDepth-First Search Edge List:")
    path = edge_list.dfs(0,15)
    edge_list.printPathD(path,15)
    print()
    end = time.time()
    print("Running time for DFS using an Edge List:", end-start,"\n")
    
    #drawing each graph
    graph.draw()
    matrix.draw()
    edge_list.draw()
   