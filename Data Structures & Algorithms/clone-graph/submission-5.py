"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
    # we want to clone the graph without returning the graph
    # so we can build this dfs or bfs. we always need to return the first node of the graph
    #  first node is 1

        oldToNew = {}

    #dfs we go deep and backtrack, if we seen the node already we obviously dont want to go through it so that is the base case. I guess None is a base case?
        def dfs(node, oldToNew):
            
            # if its already there we want to return it as is and not as None because we'll mess up the graph 
            # return the hashmap one as it is the new oen
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy #saving before we do recursion? 
            
            # lets traverse through the neighbours and perform dfs
            for n in node.neighbors:
                copy.neighbors.append(dfs(n, oldToNew))
                
            return copy

        return dfs(node, oldToNew) if node else None