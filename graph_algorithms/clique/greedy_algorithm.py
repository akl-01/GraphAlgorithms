from graph_algorithms.GraphRepresent import GraphRepresent
from graph_algorithms.ResultsWrapper import CliqueWrapper
import numpy as np
import copy

def smallest_degree_sorting(graph: GraphRepresent):
    _graph = copy.deepcopy(graph)
    sorted_vertices = []
    number_vertex = _graph.number_vertex

    while len(sorted_vertices) < number_vertex:
        _graph.sorting_by_degree()
        idx, degree = _graph.min_degree
        sorted_vertices.append(idx)
        _graph.drop_vertex(str(idx))

    return sorted_vertices    

def find_clique_sds(graph: GraphRepresent):
    sorted_vertices = smallest_degree_sorting(graph)[::-1]
    clique = []
    start_vertex = sorted_vertices[0]
    clique.append(start_vertex)
    
    for v_sorted in sorted_vertices[1:]:
        flag = True
        for v_clique in clique:
            if v_sorted not in graph.neighbors(str(v_clique)):
                flag = False
                break
        if flag == True:
            clique.append(v_sorted)
    
    _sorted_vertices = sorted_vertices[::-1]
    _clique = []
    _start_vertices = _sorted_vertices[0]
    clique.append(_start_vertices)

    for v_sorted in _sorted_vertices[1:]:
        flag = True
        for v_clique in _clique:
            if v_sorted not in graph.neighbors(str(v_clique)):
                flag = False
                break
        if flag == True:
            _clique.append(v_sorted)

    return CliqueWrapper(clique) if len(clique) >= len(_clique) else CliqueWrapper(_clique)

def degree_sorting(vertices: list, graph: GraphRepresent):
    return sorted(vertices, key=lambda v: len(graph.neighbors(v)))[::-1]

def greedy_randomize_clique(graph: GraphRepresent, iterations: int=10):
    best_clique = []
    sorted_vertices = degree_sorting(graph.vertices, graph)

    for vertex in sorted_vertices:
        if len(graph.neighbors(vertex)) <= len(best_clique):
            return CliqueWrapper(best_clique)
        for _ in range(iterations):
            clique = [vertex]
            clique_candidates = graph.neighbors(vertex)
            np.random.shuffle(clique_candidates)

            for v_candidate in clique_candidates:
                flag = True
                for v_clique in clique:
                    if v_candidate not in graph.neighbors(str(v_clique)):
                        flag = False
                        break
                if flag == True:
                    clique.append(v_candidate)

            if len(clique) > len(best_clique):
                best_clique = clique
    return CliqueWrapper(best_clique)

def greedy_clique(graph: GraphRepresent):
    best_clique = []
    sorted_vertices = degree_sorting(graph.vertices, graph)

    for vertex in sorted_vertices:
        clique = [vertex]
        clique_candidates = graph.neighbors(vertex)
        clique_candidates = degree_sorting(clique_candidates, graph)

        for v_candidate in clique_candidates:
            flag = True
            for v_clique in clique:
                if v_clique not in graph.neighbors(str(v_candidate)):
                    flag = False
                    break
            if flag == True:
                clique.append(v_candidate)

        if len(clique) > len(best_clique):
            best_clique = clique
    return CliqueWrapper(best_clique)