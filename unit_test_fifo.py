import unittest
from FIFO_improved import MaxFlow
from problem_generator_improved import DirectedGraph, generate_random_graph

# Assuming you have already imported MaxFlow and DirectedGraph

class TestMaxFlow(unittest.TestCase):
    def setUp(self):
        # Create a simple graph for testing
        self.graph = DirectedGraph(6)
        # Example graph structure (for testing)
        # (source, destination, capacity)
        edges = [
            (0, 1, 16),
            (0, 2, 13),
            (1, 2, 10),
            (1, 3, 12),
            (2, 1, 4),
            (2, 4, 14),
            (3, 2, 9),
            (3, 5, 20),
            (4, 3, 7),
            (4, 5, 4)
        ]

        # Add edges to the graph
        for u, v, w in edges:
            self.graph.addEdge(u, v, w)

        # Initialize MaxFlow object
        self.max_flow_solver = MaxFlow(self.graph, 0, 5)  # Source is 0, sink is 5

    def test_max_flow(self):
        expected_flow = 23  # The expected max flow for the provided graph
        actual_flow = self.max_flow_solver.FIFOPushRelabel()
        self.assertEqual(actual_flow, expected_flow, f"Expected max flow: {expected_flow}, but got: {actual_flow}")

    def test_no_path(self):
        # Test case where no path exists from source to sink
        disconnected_graph = DirectedGraph(2)
        #disconnected_graph.addEdge(0, 1, 10)

        no_path_solver = MaxFlow(disconnected_graph, 0, 1)
        actual_flow = no_path_solver.FIFOPushRelabel()
        self.assertEqual(actual_flow, 0, "Expected flow should be 0 when there is no path from source to sink.")

    def test_zero_capacity_edge(self):
        # Test case with zero capacity edge
        zero_capacity_graph = DirectedGraph(4)
        zero_capacity_graph.addEdge(0, 1, 10)
        zero_capacity_graph.addEdge(1, 2, 0)  # Zero capacity edge
        zero_capacity_graph.addEdge(2, 3, 10)

        zero_capacity_solver = MaxFlow(zero_capacity_graph, 0, 3)
        actual_flow = zero_capacity_solver.FIFOPushRelabel()
        self.assertEqual(actual_flow, 0, "Expected flow should be 10 despite zero capacity edge.")


if __name__ == '__main__':
    unittest.main()
    print("tutt ok")

