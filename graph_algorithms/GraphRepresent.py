import re
from collections import defaultdict
from pathlib import Path

class GraphRepresent:
    def __init__(self, file: Path):
        self.graph_dict = defaultdict(list)
        if not isinstance(file, Path):
            raise TypeError("{} file need to be a Path type".format(file))
        self.read(file)
        self.degrees = {str(v): len(self.graph_dict[v]) for v in self.vertices}

    def read(self, file: Path):
        edge_pattern = r'e \d+ \d+'
        compiled_edge_pattern = re.compile(edge_pattern)

        with open(file, "r") as f:
            for file_line in f.readlines():
                match = compiled_edge_pattern.match(file_line)
                if match:
                    list_file_line = match.group().split(" ")
                    vertex_1 = list_file_line[1]
                    vertex_2 = list_file_line[2]

                    if vertex_1 not in self.graph_dict[vertex_2]:
                        self.graph_dict[vertex_2].append(vertex_1)
                    if vertex_2 not in self.graph_dict[vertex_1]:
                        self.graph_dict[vertex_1].append(vertex_2)

    def neighbors(self, vertex: str):
        return self.graph_dict[vertex]
    
    def drop_vertex(self, vertex: str) -> list:
        _vertices = self.vertices
        for v in _vertices:
            if vertex in self.graph_dict[v]:
                self.graph_dict[v].remove(vertex)
                self.degrees[v] -= 1
        del self.graph_dict[vertex]
        del self.degrees[vertex]


    @property
    def vertices(self):
        return [vertex for vertex in self.graph_dict.keys()]
    
    @property
    def number_vertex(self):
        return len(self.graph_dict.keys())
    
    @property
    def number_edges(self):
        _number_edges = 0
        for vertex in self.graph_dict.keys():
            _number_edges += len(self.graph_dict[vertex])
        
        return _number_edges // 2 
    
    def sorting_by_degree(self):
        self.degrees = dict(sorted(self.degrees.items(), key=lambda item: item[1]))
    
    @property
    def vertex_degrees(self):
        return self.degrees

    @property
    def min_degree(self):
        key = list(self.degrees.keys())[0]
        value = self.degrees[key]
        return key, value

