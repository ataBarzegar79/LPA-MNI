from graph import Graph


class LpaMni:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def execute_algorithm(self):
        self.initialize_unique_label_for_each_node(self.graph.get_nodes())
        nodes_with_degree_centrality_rate = self.get_nodes_based_on_degree_centrality_in_descending_order()
        self.calculate_initial_commuinities_by_modularity_measure(nodes_with_degree_centrality_rate)
        self.calculate_final_communities_based_on_basic_lpa()

    def initialize_unique_label_for_each_node(self, nodes: list):
        pass

    def get_nodes_based_on_degree_centrality_in_descending_order(self) -> list:
        pass

    def calculate_initial_commuinities_by_modularity_measure(self, nodes_with_degree_centrality_rate) -> None:
        pass

    def calculate_final_communities_based_on_basic_lpa(self) -> None:
        pass

    def check_if_community_labels_stayed_steady_in_current_and_previous_iteration(
            self,
            current: dict,
            previous: dict
    ) -> bool:
        pass
