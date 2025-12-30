import argparse
from input import get_matrix_from_input

#functions
"""
OPERATIONS = {
    'gram-schmidt': gram_schmidt,
    'rref': rref,
    'ref': ref,
    'nullspace': nullspace,
    'column-space': column_space,
}
"""
def main():
    parser = argparse.ArgumentParser(
        description="A simple linear algebra CLI.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Available operations:
  gram-schmidt    Gram-Schmidt orthogonalization
  rref            Reduced row echelon form
  ref             Row echelon form
  nullspace       Null space basis
  column-space    Column space basis

Example:
  "linalg rref"
  (then enter your matrix with columns seperated by spaces and rows seperated by new lines)
        """
    )

    parser.add_argument(
        'operation',
        choices=['rref'], #switch to OPERATIONS.keys() later
        help='Operation to perform'
    )

    args = parser.parse_args()
