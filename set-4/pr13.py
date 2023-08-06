# 13. **Breadth First Search (BFS)**: Implement BFS for a graph in Python.
#     - *Input*: A graph
#     - *Output*: Vertices visited in BFS order


from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        if start not in self.graph:
            return []

        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                if node in self.graph:
                    queue.extend(self.graph[node])

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
result = graph.bfs(start_vertex)
print(result)
