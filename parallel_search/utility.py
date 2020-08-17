from glob import glob
from functools import reduce
from operator import or_
import string
import random


def combine_sets(sets: [set]):
    return reduce(or_, sets)


def random_list(
    count: int,
    length: int,
    ignore_count=10000,
    ignore_func=None
):
    rs = 0
    for n in range(count):
        value = ''.join(
            random.choices(
                string.ascii_lowercase + string.digits,
                k=length
            )
        ) + '\n'
        if ignore_func is None and ignore_func(value):
            rs = rs + 1
            if rs % ignore_count == 0:
                yield value
        else:
            yield value


def read_list(path: str):
    for line in open(path, 'r'):
        yield line


def get_paths(args: [str]):
    paths = []
    for expr in args:
        paths = paths + glob(expr)
    return paths


def set_of_strings_beginning_with_char(list: [str], char: str):
    initial_set = set()
    for item in list:
        try:
            if item[0] is char:
                initial_set.add(item)
        except IndexError:
            pass
    return initial_set
