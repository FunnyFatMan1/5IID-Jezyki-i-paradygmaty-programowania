import numpy as np

def matrix_operations(operations):
    def validate(operation, matrices):
        if operation == "add" or operation == "multiply":
            return all(mat.shape == matrices[0].shape for mat in matrices)
        elif operation == "transpose":
            return True
        return False

    def execute(operation, matrices):
        if operation == "add":
            return sum(matrices)
        elif operation == "multiply":
            result = matrices[0]
            for mat in matrices[1:]:
                result = result * mat
            return result
        elif operation == "transpose":
            return [mat.T for mat in matrices]

    return validate, execute
