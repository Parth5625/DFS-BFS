import networkx as nx
import matplotlib.pyplot as plt

def generate_tree(nodes, children_per_node):
    G = nx.Graph()
    node_count = 0
    queue = [0]
    while node_count < nodes:
        parent = queue.pop(0)
        for _ in range(children_per_node):
            node_count += 1
            G.add_edge(parent, node_count)
            queue.append(node_count)
    return G

def visualize_bfs_graph(G):
    # Perform BFS traversal
    bfs_tree = nx.bfs_tree(G, source=0)
    bfs_nodes = list(bfs_tree.nodes())
    levels = {0: 0}
    queue = [0]
    
    # Determine the level for each node
    while queue:
        current_node = queue.pop(0)
        current_level = levels[current_node]
        for neighbor in G.neighbors(current_node):
            if neighbor not in levels:
                levels[neighbor] = current_level + 1
                queue.append(neighbor)
    
    # Define position based on levels
    pos = {node: (level, i) for i, (node, level) in enumerate(sorted(levels.items(), key=lambda x: x[1]))}
    
    # Create a color map based on BFS traversal order
    node_color_map = [bfs_nodes.index(node) for node in G.nodes()]

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_color_map, cmap=plt.get_cmap('Blues'), font_size=12, font_weight="bold")
    plt.title("Visualization of a Tree (BFS)")
    plt.show()

# Generate a tree with 20 nodes, each having 2 children
tree = generate_tree(nodes=20, children_per_node=2)

# Visualize the tree using BFS
visualize_bfs_graph(tree)
