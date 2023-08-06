# 12. **Depth First Search (DFS)**: Implement DFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in DFS order


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)
            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)

        dfs_recursive(start)
        return result


# Test the function
# Example graph:   1 --- 2
#                 |     |
#                 4 --- 3
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

start_vertex = 1
result = graph.dfs(start_vertex)
print(result)
