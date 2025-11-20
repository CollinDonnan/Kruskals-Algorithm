# Kruskal's Algorithm

This repository contains an implementation of **Kruskal's algorithm** in Python.  
Kruskal's algorithm is a greedy algorithm used to find the **minimum spanning tree (MST)** of a weighted graph.  
This implementation assumes edges are represented as tuples in the form:


## How It Works

1. **Sort all edges** in ascending order by weight.  
2. **Select the smallest edge**. If adding the edge does **not** create a cycle, include it in the MST.  
3. **Repeat** this process until the MST contains **V − 1 edges**, where *V* is the number of vertices.  
4. A **union–find (disjoint-set)** data structure is used to efficiently detect cycles.

