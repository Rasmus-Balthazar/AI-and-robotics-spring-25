class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = set()
        self.edges = []
    
    def add_node(self, node):
        self.nodes.add(node)
        self.graph[node] = []
        
    def add_edge(self, node1, node2, value):
        if(node1 not in self.graph):
            self.add_node(node1)
        if(node2 not in self.graph):
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)
        self.edges.append((node1, node2), value)
    

    def get_neighbors(self, node):
        return self.graph[node]
    
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges
    
    def __str__(self):
        return str(self.graph)
    
    def __repr__(self):
        return str(self.graph)

class Planner:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.queue = []
        self.parent = {}
        self.queue.append(start)
        self.parent[start] = None
        
    def bfs(self):
        while self.queue:
            node = self.queue.pop(0)
            if node == self.goal:
                break
            self.visited.add(node)
            for neighbor in self.graph.get_neighbors(node):
                if neighbor not in self.visited:
                    self.queue.append(neighbor)
                    self.parent[neighbor] = node
        return self.parent
    
    def get_path(self):
        path = []
        node = self.goal
        while node is not None:
            path.append(node)
            node = self.parent[node]
        return path[::-1]
    
    def generate_graph(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.graph.add_node((i, j))
        return self.graph
    
    def __str__(self):
        return str(self.parent)
    
    def __repr__(self):
        return str(self.parent)

if __name__ == "__main__":
    graph = Graph()
    planner = Planner(graph, (0, 0), (3, 3))
    matrix = [[0, 0, 0, 0],
              [0, 1, 0, 1],
              [0, 0, 0, 0],
              [0, 1, 0, 0]]
    graph = planner.generate_graph(matrix)
    planner.bfs()
    # print(planner.get_path())
    # print(planner)
    # print(graph)
    # print(graph.get_nodes())
    # print(graph.get_edges())