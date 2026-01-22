import networkx as nx
from collections import *
import matplotlib.pyplot as plt 
class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None
        
        Be sure that your code can handle possible edge cases, e.g.:
            running bfs traversal on an empty graph
            running bfs traversal on an unconnected graph
            running bfs from a start node that does not exist in the graph
            running bfs search for an end node that does not exist in the graph
            any other edge cases you can think of

        """
        #edge cases-------------------------------
        # for an empty graph
        if len(self.graph.nodes()) == 0:
            return None 
        # for running bfs from a start node that does not exist in the graph
        if start not in self.graph.nodes():
            return None 
        # raise exception for end node
        if end == '':
            raise ValueError("End node cannot be empty string")
        # if end node input and a path does not exist, return None
        if end is not None and end not in self.graph.nodes():
            return None
        
        
        # initialize lists -----------------------
        # visited for all nodes already ... visited
        visited = []     
        # queue for all that have not been visited 
        queue = deque([start])   
        #parent node 
        parent = {start: None}
        
        # traversal -------------------------------
        # loop through as long as there are still nodes to be checked 
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                # adds node to list of checked nodes 
                visited.append(node)
                
            # add the neighbors that have not been visited to the queue to BE visited
            for neighbor in self.graph.neighbors(node):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    parent[neighbor] = node 
                    
            if end is not None and node == end:
                path = []
                current = end
                while current is not None:
                        path.append(current)
                        current = parent[current]
                return path[::-1]
                    
        # if end node does not exist and therefore no path exists 
        if end is not None: 
            return None
        # if no end is specified return the output 
        return visited
                

        


"""
References:
https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
"""