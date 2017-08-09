import networkx as nx


def run():
    # x = input('Enter the graph in the format: AD4, DE1, EC8, ...\n')
    # print(x + "xd")

    edges = [('a', 'd', 4), ('d', 'e', 1), ('e', 'c', 8), ('c', 'b', 2), ('b', 'a', 6), ('a', 'c', 9), ('d', 'f', 7),
             ('f', 'c', 5), ('f', 'e', 9), ('b', 'd', 3), ('f', 'a', 3)]

    customers_routes = nx.DiGraph()
    customers_routes.add_weighted_edges_from(edges)

    print(customers_routes.get_edge_data('a', 'd')['weight'] + customers_routes.get_edge_data('d', 'e')['weight'])
    print(customers_routes.get_edge_data('a', 'f')['weight'] + customers_routes.get_edge_data('f', 'e')['weight'])
    print(customers_routes.get_edge_data('e', 'c')['weight'] + customers_routes.get_edge_data('c', 'b')['weight'])
