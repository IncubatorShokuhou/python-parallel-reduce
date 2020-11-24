import more_itertools as mit
from itertools import repeat
from functools import reduce,wraps
import multiprocessing
__version__ = '0.0.2'


def reduce_p(function, sequence, n_jobs=multiprocessing.cpu_count(), initial=None):
    if n_jobs == 1:
        return reduce(function, sequence, initial)
    else:
        sliced_sequence = mit.distribute(n_jobs, sequence)
        with multiprocessing.Pool(n_jobs) as pool:
            new_sequence = pool.starmap(reduce, zip(
                repeat(function), sliced_sequence, repeat(initial)))
        return reduce(function, new_sequence, initial)

def handle_none(function):
    @wraps(function)
    def wrapper_function(i,j):
        if i == None:
            if j == None:
                return None
            else:
                return j
        else:
            if j == None:
                return i
            else:
                return function(i, j)
    return wrapper_function
