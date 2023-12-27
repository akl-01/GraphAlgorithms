from collections import defaultdict


class ColoringWrapper:
    def __init__(self, colors: dict):
        self._colors_vertices = colors
    
    @property
    def amount_colors(self):
        return len(set(self.colors_vertices.values()))
    
    @property
    def colors_vertices(self):
        return self._colors_vertices

class CliqueWrapper:
    def __init__(self, clique: list):
        self._clique = clique
    
    @property
    def clique_size(self):
        return len(self._clique)