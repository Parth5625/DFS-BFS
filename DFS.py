import networkx as nx
import matplotlib.pyplot as plt

def generate_tree(nodes, children_per_node):
    G = nx.Graph()
    node_count = 0
    queue = [0]
    G.add_node(0) 
    while node_count < nodes - 1:
        parent = queue.pop(0)
        for _ in range(children_per_node):
            node_count += 1
            G.add_node(node_count)
            G.add_edge(parent, node_count)
            queue.append(node_count)
    return G

def visualize_dfs_graph(G):
    dfs_tree = nx.dfs_tree(G, source=0)
    dfs_nodes = list(dfs_tree.nodes())
    levels = {0: 0}
    stack = [0]
   
    while stack:
        current_node = stack.pop()
        current_level = levels[current_node]
        for neighbor in reversed(list(G.neighbors(current_node))):  # reversed to maintain DFS order
            if neighbor not in levels:
                levels[neighbor] = current_level + 1
                stack.append(neighbor)
  
    pos = {node: (level, i) for i, (node, level) in enumerate(sorted(levels.items(), key=lambda x: x[1]))}

    node_color_map = [dfs_nodes.index(node) for node in G.nodes()]

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_color_map, cmap=plt.get_cmap('Blues'), font_size=12, font_weight="bold")
    plt.title("Visualization of a Tree (DFS)")
    plt.show()

tree = generate_tree(nodes=20, children_per_node=2)

visualize_dfs_graph(tree)
