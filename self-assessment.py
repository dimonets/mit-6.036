def add_two_lists(a, b):
    """
    Adds two lists element-wise.
    
    Args:
        a (list): First list of numbers
        b (list): Second list of numbers (must be same length as a)
    
    Returns:
        list: New list where each element is the sum of corresponding elements
    """
    return [a[i]+b[i] for i in range(len(a))]

def dot(v1, v2):
    """
    Computes the dot product of two vectors.
    
    Args:
        v1 (list): First vector
        v2 (list): Second vector (must be same length as v1)
    
    Returns:
        float: The dot product of v1 and v2
    """
    return sum(v1[i]*v2[i] for i in range(len(v1)))

def add_n(n):
    """
    Creates a function that adds a constant n to each element of a list.
    
    Args:
        n (number): The constant to add to each element
    
    Returns:
        function: A function that takes a list and returns a new list with n added to each element
    """
    def new_fun(v):
        return [elt + n for elt in v]
    return new_fun

def array_mult(A, B):
    """
    Performs matrix multiplication of two matrices A and B.
    
    Args:
        A (list of lists): First matrix
        B (list of lists): Second matrix (number of columns must match number of rows in A)
    
    Returns:
        list of lists: The resulting matrix product
    
    Raises:
        AssertionError: If dimensions are incompatible for matrix multiplication
    """
    A_n = len(A) 
    A_m = len(A[0])
    B_n = len(B)
    B_m = len(B[0])
    assert A_m == B_n

    R_n = A_n
    R_m = B_m
    R = [[0 for j in range(R_m)] for i in range(R_n)]

    def row(M, r): return M[r]
    def col(M, c): return [v[c] for v in M]
    def dot(v1, v2): return sum([x*y for x, y in zip(v1, v2)])

    for i in range(R_n):
        for j in range(R_m):
            R[i][j] = dot(row(A,i), col(B,j))
    return R

a = [1, 2, 3]
b = [4, 5, 6]

M1 = [[1, 2, 3], [-2, 3, 7]]
M2 = [[1,0,0],[0,1,0],[0,0,1]]
M3 = [[1], [0], [-1]]

print(add_two_lists(a, b))
print(dot(a, b))
print(add_n(10)([1, 5, 3]))

print(array_mult(M1, M2))
print(array_mult(M1, M3))

