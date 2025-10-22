def recursive_function(n, depth=0, max_depth=10):
    ## Prevent excessive recursion
    if depth >= max_depth:
        return None

    ## Recursive logic
    if n > 0:
        return recursive_function(n - 1, depth + 1, max_depth)
    return n