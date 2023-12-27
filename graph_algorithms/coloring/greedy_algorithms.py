from ..GraphRepresent import GraphRepresent
from ..ResultsWrapper import ColoringWrapper
import copy

def get_vertex_color(vertex_neighbors: list, colors: dict):
    color = 0
    neighbors_colors = [colors[neighbor] for neighbor in vertex_neighbors]

    while True:
        if color not in neighbors_colors:
            return color
        color += 1

def smallest_degree_sorting(graph: GraphRepresent):
    _graph = copy.deepcopy(graph)
    sorted_vertices = []
    sorted_degrees = []
    number_vertex = _graph.number_vertex

    while len(sorted_vertices) < number_vertex:
        _graph.sorting_by_degree()
        idx, degree = _graph.min_degree
        sorted_vertices.append(idx)
        sorted_degrees.append(degree)
        _graph.drop_vertex(str(idx))

    return sorted_vertices

def greedy_graph_coloring(graph: GraphRepresent):

    colors = {vertex: None for vertex in graph.vertices}

    for vertex in graph.vertices:
        colors[vertex] = get_vertex_color(graph.neighbors(vertex), colors)
    
    coloring_wrapper = ColoringWrapper(colors)
    return coloring_wrapper

def smallest_degree_sorting_coloring(graph: GraphRepresent):
    colors = {vertex: None for vertex in graph.vertices}

    sorted_vertices = smallest_degree_sorting(graph)[::-1]
    
    for v_sorted in sorted_vertices:
        colors[v_sorted] = get_vertex_color(graph.neighbors(v_sorted), colors)
    
    _colors = {vertex: None for vertex in graph.vertices}
    _sorted_vertices = sorted_vertices[::-1]
    for v_sorted in _sorted_vertices:
        _colors[v_sorted] = get_vertex_color(graph.neighbors(v_sorted), _colors) 

    colors_wrapper = ColoringWrapper(colors)
    _colors_wrapper = ColoringWrapper(_colors)
    return colors_wrapper if colors_wrapper.amount_colors < _colors_wrapper.amount_colors else _colors_wrapper
     


    
