from pathlib import Path

class GraphRepresent:
    def __init__(self, file: Path):
        self.graph_dict = dict()
        if not isinstance(file, Path):
            raise TypeError("{} file need to be a Path type".format(file))
        self.read(file)

    def read(self, file: Path):
        