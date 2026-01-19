# write tests for bfs
import pytest
from search.graph import Graph

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
    graph_object = Graph(data)
    G = graph_object.graph
    
    # what are we looking for 
    result = G.bfs('31806696;Luke Gilbert')  
    
    # test that graph is being made and reads nodes 
    assert len(G.nodes()) > 0 
    
    # test that both numbers and names as str can be interpreted / handled 
    assert 'Luke Gilbert' in G.graph.nodes()
    assert '31806696' in G.graph.nodes()
    
    assert isinstance(result, list)
    assert result[0] == '31806696;Luke Gilbert'
    

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
    pass
