import networkx as nx
import matplotlib.pyplot as plt

# Ініціалізуємо граф
G = nx.Graph()

# Вершини (зупинки)
stops = [
    "Центр", "Залізничний вокзал", "Університет", "Площа Ринок",
    "Парк", "Театр", "Стадіон", "ТЦ Форум", "Обласна лікарня"
]
G.add_nodes_from(stops)

# Ребра з вагами (відстань у хвилинах)
weighted_edges = [
    ("Центр", "Площа Ринок", 5),
    ("Центр", "Університет", 7),
    ("Центр", "ТЦ Форум", 10),
    ("Університет", "Залізничний вокзал", 8),
    ("Університет", "Театр", 6),
    ("Площа Ринок", "Парк", 4),
    ("Парк", "Обласна лікарня", 9),
    ("Театр", "Стадіон", 5),
    ("ТЦ Форум", "Залізничний вокзал", 6),
    ("Стадіон", "Обласна лікарня", 7),
]

G.add_weighted_edges_from(weighted_edges)
plt.figure(figsize=(12, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа з вагами (в хвилинах)")
plt.show()
# Знаходимо найкоротші шляхи між усіма парами вершин
all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
all_shortest_lengths = dict(nx.all_pairs_dijkstra_path_length(G, weight='weight'))

# Виводимо результати
for start in G.nodes:
    print(f"\n🔹 Найкоротші шляхи від '{start}':")
    for end in G.nodes:
        if start != end:
            path = all_shortest_paths[start][end]
            length = all_shortest_lengths[start][end]
            print(f"  до '{end}': шлях = {path}, довжина = {length} хв")