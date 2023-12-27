import time
from pathlib import Path
import pandas as pd

from graph_algorithms.GraphRepresent import GraphRepresent
from graph_algorithms.coloring.greedy_algorithms import (greedy_graph_coloring, 
                                                           smallest_degree_sorting_coloring)

def print_result(result: dict):
    indexes = list(result.keys())
    color_amount = [list(result.values())[i][1] for i in range(len(result))]
    times = [list(result.values())[i][0] for i in range(len(result))]
    result_df = pd.DataFrame({"amount_color": color_amount, "time": times}, index=indexes)
    result_df.to_excel("results/coloring.xlsx")
    print(result_df)

def main():
    test_files = [
        "myciel3.col",
        "myciel7.col",
        "school1.col",
        "school1_nsh.col",
        "anna.col",
        "miles1000.col",
        "miles1500.col",
        "le450_5a.col",
        "le450_15b.col",
        "queen11_11.col"
    ]

    greedy_functions = [
        greedy_graph_coloring
    ]

    tests_result = {}

    for greedy_function in greedy_functions:
        for test_file in test_files:
            total_coloring_time = 0
            full_path = Path("./data/coloring").joinpath(test_file).resolve()
            graph_represent = GraphRepresent(Path(full_path))

            start_coloring_time = time.time()
            coloring_wrapper = greedy_function(graph_represent)
            total_coloring_time += time.time() - start_coloring_time

            tests_result[test_file] = [total_coloring_time, coloring_wrapper.amount_colors]
    print_result(tests_result)
    

if __name__ == "__main__":
    main()

