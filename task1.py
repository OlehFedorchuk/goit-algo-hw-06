import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (зупинки)
stops = [
    "Центр", "Залізничний вокзал", "Університет", "Площа Ринок",
    "Парк", "Театр", "Стадіон", "ТЦ Форум", "Обласна лікарня"
]
G.add_nodes_from(stops)

# Додаємо ребра (дороги між зупинками)
edges = [
    ("Центр", "Площа Ринок"),
    ("Центр", "Університет"),
    ("Центр", "ТЦ Форум"),
    ("Університет", "Залізничний вокзал"),
    ("Університет", "Театр"),
    ("Площа Ринок", "Парк"),
    ("Парк", "Обласна лікарня"),
    ("Театр", "Стадіон"),
    ("ТЦ Форум", "Залізничний вокзал"),
    ("Стадіон", "Обласна лікарня"),
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, edge_color='gray')
plt.title("Транспортна мережа міста")
plt.show()

# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Ступінь кожної вершини
degrees = dict(G.degree())

# Вивід
print("Кількість зупинок (вершин):", num_nodes)
print("Кількість доріг (ребер):", num_edges)
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"  {node}: {degree}")