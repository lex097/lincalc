from sympy import Matrix

def rref(matrix):
    rref_form, pivot_cols = matrix.rref()

    return rref_form