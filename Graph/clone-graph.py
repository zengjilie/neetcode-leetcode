# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        map = {}

        def bfs(node):
            q = collections.deque()
            q.append(node)

            while q:
                node = q.popleft()
                if node not in map:
                    map[node] = Node(node.val)

                for neighbor in node.neighbors:
                    if neighbor not in map:
                        map[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    map[node].neighbors.append(map[neighbor])

        bfs(node)
        return map[node]

# time complexity O(num_nodes*num_edges)
# space complexity O(num_nodes)

# caveat
# the input could be none

# summary
# the key to solve this problem is hashmap + bfs/dfs