import time
from pathlib import Path
import pandas as pd

from graph_algorithms.GraphRepresent import GraphRepresent
from graph_algorithms.clique.greedy_algorithm import find_clique_sds, greedy_randomize_clique, greedy_clique

def print_result(result: dict, idx):
    indexes = list(result.keys())
    clique_size = [list(result.values())[i][1] for i in range(len(result))]
    times = [list(result.values())[i][0] for i in range(len(result))]
    result_df = pd.DataFrame({"time": times, "clique_size": clique_size}, index=indexes)
    result_df.to_excel("results/clique_" + str(2) + ".xlsx")

def main():
    test_files = [
        'brock200_1.clq',
        'brock200_2.clq',
        'brock200_3.clq',
        'brock200_4.clq',
        'brock400_1.clq',
        'brock400_2.clq',
        'brock400_3.clq',
        'brock400_4.clq',
        'C125.9.clq',
        'gen200_p0.9_44.clq',
        'gen200_p0.9_55.clq',
        'hamming8-4.clq',
        'johnson16-2-4.clq',
        'johnson8-2-4.clq',
        'keller4.clq',
        'MANN_a27.clq',
        'MANN_a9.clq',
        'p_hat1000-1.clq',
        'p_hat1000-2.clq',
        'p_hat1500-1.clq',
        'p_hat300-3.clq',
        'p_hat500-3.clq',
        'san1000.clq',
        'sanr200_0.9.clq',
        'sanr400_0.7.clq'
    ]

    greedy_functions = [
        find_clique_sds
    ]

    tests_result = {}

    for idx, greedy_function in enumerate(greedy_functions):
        print(idx)
        for test_file in test_files:
            print("file = {}".format(test_file))
            total_coloring_time = 0
            full_path = Path("./data/clique").joinpath(test_file).resolve()
            graph_represent = GraphRepresent(Path(full_path))

            start_coloring_time = time.time()
            clique_wrapper = greedy_function(graph_represent)
            total_coloring_time += time.time() - start_coloring_time

            tests_result[test_file] = [total_coloring_time, clique_wrapper.clique_size]
    print_result(tests_result, idx)
    

if __name__ == "__main__":
    main()

