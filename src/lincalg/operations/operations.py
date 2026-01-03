from typing import Union, List
from sympy import Matrix, GramSchmidt

def rref(matrix: Matrix) -> Matrix:
    rref_form, pivot_cols = matrix.rref()

    return rref_form

def ref(matrix: Matrix) -> Matrix:
    return matrix.echelon_form()

def gram_schmidt(matrix: Matrix) -> List[Matrix]:
    return GramSchmidt(matrix, True) #normalized

def column_space(matrix: Matrix) -> List[Matrix]:
    return matrix.columnspace()

def nullspace(matrix: Matrix) -> List[Matrix]:
    return matrix.nullspace()