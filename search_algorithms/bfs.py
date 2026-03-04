from collections import deque

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):

    visited=set()
    queue=deque([start])

    print("BFS Traversal:")

    while queue:

        node=queue.popleft()

        if node not in visited:

            print(node,end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                queue.append(neighbour)

bfs('A')
