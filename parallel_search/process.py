from multiprocessing import Pool
from .utility import set_of_strings_beginning_with_char, read_list


def process_synchronous(paths: [str]):
    sets = []
    for path in paths:
        sets.append(set_of_strings_beginning_with_char(read_list(path), 'r'))
    return sets


def process_file_path(path: str, char: str):
    list = read_list(path)
    return set_of_strings_beginning_with_char(list, char)


def process_files(paths: [str], processes: int):
    pool = Pool(processes=processes)
    result_promises = [
        pool.apply_async(process_file_path, (path, 'r'))
        for path in paths
    ]
    return [res.get() for res in result_promises]
