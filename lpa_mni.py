from graph import Graph


class LpaMni:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def execute_algorithm(self):
        self.initialize_unique_label_for_each_node(self.graph.get_nodes())
        nodes_with_degree_centrality_rate = self.get_nodes_based_on_degree_centrality_in_descending_order()
        self.calculate_initial_commuinities_by_modularity_measure(nodes_with_degree_centrality_rate)
        self.calculate_final_communities_based_on_basic_lpa(nodes_with_degree_centrality_rate)

    def initialize_unique_label_for_each_node(self, nodes: list) -> None:
        for node in nodes:
            self.graph.set_label_to_node(label=str(node), node=node)

    def get_nodes_based_on_degree_centrality_in_descending_order(self) -> list:
        nodes_with_degree_centrality = self.graph.sort_graph_based_on_degree_centrality()
        sorted_items = sorted(nodes_with_degree_centrality.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items]

    def calculate_initial_commuinities_by_modularity_measure(self, nodes_with_degree_centrality_rate) -> None:
        while True:
            modularity_at_start = self.graph.calculate_modularity()
            for node in nodes_with_degree_centrality_rate:
                gained_modularities = dict()
                node_current_label = self.graph.get_node_current_label(node=node)
                gained_modularities[node_current_label] = self.graph.calculate_modularity()
                node_neighbours = self.graph.get_node_neighbours(node=node)
                for neighbour in node_neighbours:
                    neighbour_label = self.graph.get_node_current_label(node=neighbour)
                    self.graph.set_label_to_node(
                        label=neighbour_label,
                        node=node
                    )
                    gained_modularities[neighbour_label] = self.graph.calculate_modularity()
                self.graph.set_label_to_node(
                    label=self.get_label_with_most_modularity(gained_modularities),
                    node=node
                )
            modularity_at_final = self.graph.calculate_modularity()
            if modularity_at_final == modularity_at_start:
                break

    def calculate_final_communities_based_on_basic_lpa(self, nodes_with_degree_centrality_rate: list) -> None:
        for node in nodes_with_degree_centrality_rate:
            self.calculate_node_final_label(node, nodes_with_degree_centrality_rate)

    def get_label_with_most_modularity(self, gained_modularities) -> str:
        return str(max(gained_modularities, key=gained_modularities.get))

    def calculate_node_final_label(self, node: int, nodes_with_degree_centrality_rate: list) -> None:
        candidate_final_labels = dict()
        node_neighbours = self.graph.get_node_neighbours(node=node)
        for neighbour in node_neighbours:
            neighbour_current_label = self.graph.get_node_current_label(node=neighbour)
            if neighbour_current_label not in candidate_final_labels:
                candidate_final_labels[neighbour_current_label] = 1
            else:
                candidate_final_labels[neighbour_current_label] += 1
        max_value = max(candidate_final_labels.values())  # Find the maximum value
        keys_with_max_value = [key for key, value in candidate_final_labels.items() if value == max_value]
        if len(keys_with_max_value) > 1:
            final_label = self.graph.get_node_current_label(
                node=nodes_with_degree_centrality_rate[
                    min(
                        [
                            nodes_with_degree_centrality_rate.index(item) for item in node_neighbours
                        ]
                    )
                ]
            )
            self.graph.set_label_to_node(label=final_label, node=node)
        else:
            self.graph.set_label_to_node(label=keys_with_max_value[0], node=node)
