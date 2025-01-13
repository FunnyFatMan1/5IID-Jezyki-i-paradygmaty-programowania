from functools import reduce
import numpy as np

def matrix_reduction(matrices, operation):
    if operation == "add":
        return reduce(lambda x, y: x + y, matrices)
    elif operation == "multiply":
        return reduce(lambda x, y: x @ y, matrices)
