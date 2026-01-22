# write tests for bfs
from search.graph import Graph


import pytest
import networkx as nx 


def test_bfs_traversal():
    
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    # input test file "tiny network adjacency list"
    data = "./data/tiny_network.adjlist"
    # make graph object and graph
    graph_object = Graph(data)
    G = graph_object.graph
    
    # sanity check to see if graph loaded correctly 
    print(f"Number of nodes: {len(G.nodes())}")
    print(f"Nodes: {list(G.nodes())[:10]}")  # Print first 10 nodes
    
    # check if start node exists
    print(f"'34272374' in nodes: {'34272374' in G.nodes()}")
    
    # see if bfs works 
    result = graph_object.bfs('34272374')
    print(f"Result: {result}")
    print(f"Result type: {type(result)}")
    
    # test that graph is being made and reads nodes 
    assert len(G.nodes()) > 0 
    
    # test that both numbers and names as str can be interpreted / handled 
    assert 'Martin Kampmann' in G.nodes()
    assert '34272374' in G.nodes()
    
    assert isinstance(result, list)
    assert result[0] != 'Martin Kampmann'
    
    #print(f"here is graph G:", (G.nodes.data))

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # create instance of Graph class using the bigger data file
    graph_object_2 = Graph("./data/citation_network.adjlist")
    #make and name graph
    woo = graph_object_2.graph
    
    #check that my test nodes exist 
    print(f"'32461654' exists: {'32461654' in woo.nodes()}")
    print(f"'Ryan Hernandez' exists: {'Ryan Hernandez' in woo.nodes()}")
    
    # check if two nodes that are connected will return a path 
    my_path = graph_object_2.bfs('32461654', 'Ryan Hernandez')
    assert my_path is not None
    assert isinstance(my_path, list)
    # check path starts with given key 
    assert my_path[0] == '32461654'
    # check path ends with given key 
    assert my_path[-1] == 'Ryan Hernandez'
    # using line numbers check that the length of path is as such 
    assert len(my_path) >= 2
    
    # verify this path is connected
    for i in range(len(my_path) - 1):
            assert woo.has_edge(my_path[i], my_path[i+1])
            
    # check nodes that are disconnected or not in graph 
    fakepath = graph_object_2.bfs('30120348', 'hell_yeah')
    assert fakepath is None
    
    # shortest path between test nodes
    shortpath = nx.shortest_path(woo, 'Atul Butte', '34919578')
    print('short path:', shortpath)
    
    # test if end node is empty 
    with pytest.raises(ValueError, match = "End node cannot be empty string"):
        graph_object_2.bfs('Atul Butte', '')
