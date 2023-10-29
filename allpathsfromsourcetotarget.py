"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""

from typing import List


def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

    # initialize a queue to store the available paths
    q = [[0]]

    # initialize a list to store the valid routes
    result = []

    # get the target
    target = len(graph) - 1

    while q:

        # pop the first guy in the queue
        path = q.pop()

        # check if the last guy in the path equals the target
        if path[-1] == target:
            
            # add the path to the result
            result.append(path)
        
        else:
            # get the neighbours of the last guy in the path
            for i in graph[path[-1]]:

                # add the path + the neighbors to the queue 
                q.append(path + [i])

    return result