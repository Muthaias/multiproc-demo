import sys
import time
from parallel_search.process import process_files, process_synchronous
from parallel_search.utility import get_paths, combine_sets


def run(method: str, paths, num_procs):
    result = [set()]
    t1 = time.time()
    if method == "sync":
        result = process_synchronous(paths)
    elif method == "file":
        result = process_files(paths, num_procs)
    t2 = time.time()
    print("method(%s): %s" % (method, t2 - t1))
    return result


if __name__ == "__main__":
    # Parse arguments
    method = sys.argv[1] if len(sys.argv) > 1 else "file"
    num_procs = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    paths = get_paths(sys.argv[3:]) if len(sys.argv) > 3 else []

    # Start processing
    results = run(method, paths, num_procs)

    # Reduce final result from list of sets
    final_set = combine_sets(results) if len(results) > 0 else []

    # Make list, sort and print
    list = [item for item in final_set]
    list.sort()
    for item in list:
        print(item.replace("\n", ""))
