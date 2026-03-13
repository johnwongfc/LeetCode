from typing import Optional
def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
    if not node:
        return None
    visited = {}
    def dfs(node):
        if not node:
            return
        if node in visited:
            return visited[node]
        visited[node] = Node(node.val)
        for neighbor in node.neighbors:
            dfs(neighbor)
            visited[node].neighbors.append(dfs(neighbor))
        return visited[node]
    return dfs(node) 