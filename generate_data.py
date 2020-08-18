import sys
import os
from parallel_search.utility import random_list


def write_list(path: str, list: [str]):
    with open(path, 'w') as fp:
        fp.writelines(list)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "data/utf8list%s.txt"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    length = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    num_files = int(sys.argv[4]) if len(sys.argv) > 4 else 1

    dirname = os.path.dirname(path % (0))
    try:
        os.makedirs(dirname, exist_ok=True)
    except OSError as e:
        print(e)
        print("Could not create directory: %s" % (dirname))
        exit()

    def ignore_func(value: str):
        return value[0] == 'r'

    for i in range(num_files):
        list = random_list(count, length, ignore_func=ignore_func, allow_count=10)
        write_list(path % i, list)
