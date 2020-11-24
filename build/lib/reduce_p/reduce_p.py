import more_itertools as mit
from itertools import repeat
from functools import reduce
import multiprocessing

def reduce_p(function, sequence, n_jobs=multiprocessing.cpu_count(), initial=None):
    if n_jobs == 1:
        return reduce(function, sequence, initial)
    else:
        sliced_sequence = mit.distribute(n_jobs, sequence)
        with multiprocessing.Pool(n_jobs) as pool:
            new_sequence = pool.starmap(reduce, zip(
                repeat(function), sliced_sequence, repeat(initial)))
        return reduce(function, new_sequence, initial)