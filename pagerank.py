import networkx as nx

def calculate_pagerank():
    G = nx.DiGraph()  # Tạo đồ thị có hướng

    # Thêm các cạnh (liên kết) vào đồ thị
    G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3)])

    # Tính toán PageRank
    pagerank = nx.pagerank(G, alpha=0.85)
    return pagerank
