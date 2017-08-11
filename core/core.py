import networkx as nx


def run():
    # x = input('Enter the graph in the format: AD4, DE1, EC8, ...\n')
    # print(x + "xd")

    edges = [('a', 'd', 4), ('d', 'e', 1), ('e', 'c', 8), ('c', 'b', 2), ('b', 'a', 6), ('a', 'c', 9), ('d', 'f', 7),
             ('f', 'c', 5), ('f', 'e', 9), ('b', 'd', 3), ('f', 'a', 3)]

    customers_routes = nx.DiGraph()
    customers_routes.add_weighted_edges_from(edges)

    f = open('routesList.txt', 'r')
    lines = f.read().split('\n')
    for line in lines:
        print_route_cost(line, customers_routes)

    # print(customers_routes.get_edge_data('a', 'd')['weight'] + customers_routes.get_edge_data('d', 'e')['weight'])
    # print(customers_routes.get_edge_data('a', 'f')['weight'] + customers_routes.get_edge_data('f', 'e')['weight'])
    # print(customers_routes.get_edge_data('e', 'c')['weight'] + customers_routes.get_edge_data('c', 'b')['weight'])


def print_route_cost(route: str, graph: nx.DiGraph):
    WEIGHT_ATTR_NAME = 'weight'

    total_route_cost = 0

    customers_in_route = route.split('-')
    route_size = len(customers_in_route)
    for i in range(0, route_size):
        if i < route_size - 1:
            parcialRoute = graph.get_edge_data(customers_in_route[i], customers_in_route[i + 1])

            if parcialRoute is None:
                print('NO SUCH ROUTE')
                return

            total_route_cost = total_route_cost + parcialRoute[WEIGHT_ATTR_NAME]

    print(total_route_cost)

run()