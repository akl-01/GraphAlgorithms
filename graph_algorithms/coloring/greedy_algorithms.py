from ..GraphRepresent import GraphRepresent
from ..ResultsWrapper import ColoringWrapper

def greedy_graph_coloring(graph: GraphRepresent):

    colors = {vertex: None for vertex in graph.vertices}

    def get_vertex_color(vertex_neighbors: list):
        color = 0
        neighbors_colors = [colors[neighbor] for neighbor in vertex_neighbors]

        while True:
            if color not in neighbors_colors:
                return color
            color += 1

    for vertex in graph.vertices:
        if colors[vertex] is None:
            colors[vertex] = get_vertex_color(graph.neighbors(vertex))
    
    coloring_wrapper = ColoringWrapper(colors)
    return coloring_wrapper

