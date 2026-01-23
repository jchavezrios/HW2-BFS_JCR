![Build Status](https://github.com/jschavrios/HW2-BFS_JCR/actions/workflows/test.yml/badge.svg)

# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment was to get BMI 203 students comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Overview of BFS 
The function bfs uses a Breadth-first search algorithm. It first takes in a graph created from an adjacency list, a start node, and an end node. 

It is able to create and traverse graphs made from adjacency list format data as readable by the python package networkx. 

This was tested on two different citation network lists. 

### How to use BFS
First, write in your data and create a graph object from it using networkx.

`data = "./path/to/my/data.adjlist"`

Then, make a graph object using the `Graph` class part of BFS

```python
graph_object = Graph("./path/to/my/data.adjlist")
graph = graph_object_2.graph
```
From there, use `networkx` commands to find nodes in the graph made from your data.