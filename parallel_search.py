import sys
from glob import glob
from functools import reduce
from operator import or_
from multiprocessing import Pool


def combine_sets(sets: [set]):
    return reduce(or_, sets)


def get_paths(args: [str]):
    """Get paths from multiple globs"""
    paths = []
    for expr in args:
        paths = paths + glob(expr)
    return paths


def set_of_strings_beginning_with_char(list: [str], char: str):
    """Find all lines starting with a specified character"""
    initial_set = set()
    for item in list:
        try:
            if item[0] is char:
                initial_set.add(item)
        except IndexError:
            pass
    return initial_set


def process_file_path(path: str, char: str):
    """Read and process a single file"""
    list = open(path, 'r')
    return set_of_strings_beginning_with_char(list, char)


def process_files(paths: [str], processes: int):
    """Processes files in parallel using a process pool."""
    pool = Pool(processes=processes)
    result_promises = [
        pool.apply_async(process_file_path, (path, 'r'))
        for path in paths
    ]
    return [res.get() for res in result_promises]


if __name__ == "__main__":
    # Parse arguments
    num_procs = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    paths = get_paths(sys.argv[2:]) if len(sys.argv) > 2 else []

    # Start processing
    results = process_files(paths, num_procs)

    # Reduce final result from list of sets
    final_set = combine_sets(results) if len(results) > 0 else []

    # Make list, sort and print
    list = [item for item in final_set]
    list.sort()
    for item in list:
        print(item.replace("\n", ""))
