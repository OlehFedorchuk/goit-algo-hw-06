import networkx as nx
from collections import deque

# Створюємо граф (транспортна мережа міста)
G = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'),
    ('C', 'D'), ('C', 'E'), ('D', 'F'),
    ('E', 'F')
]
G.add_edges_from(edges)

# BFS: Пошук у ширину
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# DFS: Пошук у глибину
def dfs(graph, start, goal, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

# Використання алгоритмів
start, goal = 'A', 'F'
bfs_path = bfs(G, start, goal)
dfs_path = dfs(G, start, goal)

# Вивід результатів
print("BFS шлях:", bfs_path)
print("DFS шлях:", dfs_path)

# Пояснення різниці
print("\nПояснення:")
print("🔹 BFS знаходить найкоротший шлях (найменше ребер).")
print("🔹 DFS може піти 'вглиб' і знайти довший шлях, залежно від порядку обходу сусідів.")