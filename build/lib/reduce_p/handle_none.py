from functools import wraps

def handle_nan(function):
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