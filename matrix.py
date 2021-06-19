import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def get_row(matrix, row):
    """
    Defines the specific row of a matrix
    """
    matrix = matrix
    row = row
        
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Defines the specific column of a matrix 
    """
    column = []
    for _ in matrix:
        column.append(_[column_number])
    return column
    
def dot_product(vector_one, vector_two):
    """
    Defines the dot product for multiplication
    """
    s = 0

    for i in range(len(vector_one)):
        s += vector_one[i] * vector_two[i]
    return s

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])
        
    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1 and self.w == 1:
            return 1/self.g[0][0]
        elif self.h == 2 and self.w == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a*d - b*c
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sum_dig = 0
        for i in range(len(self.g)):
             sum_dig += self.g[i][i]
        return sum_dig
                    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        inverse = []
        # TODO - your code here
        if self.h == 1 and self.w == 1:
            inverse.append([1/self.g[0][0]])
        elif self.h == 2 and self.w == 2:
            det = self.determinant()
            if det == 0:
                raise(NotImplementedError, "Determinant is 0, so inverse cannot be calculated.")
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            inverse = [[d,-b], [-c,a]]
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = 1/det * inverse[i][j]
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for i in range(len(self.g[0])):
            row_transpose = []
            for j in range(len(self.g)):
                row_transpose.append(self.g[j][i])
            matrix_transpose.append(row_transpose)
        return Matrix(matrix_transpose)
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        add_mat = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j] + other.g[i][j])
            add_mat.append(row)
        return Matrix(add_mat)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negative = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(-self.g[i][j])
            negative.append(row)
        return Matrix(negative)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        sub_mat = []
        for i in range(len(self.g)):
            row = []
            for j in range(len(self.g[0])):
                row.append(self.g[i][j] - other.g[i][j])
            sub_mat.append(row)
        return Matrix(sub_mat)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        m_rows = len(self.g)
        p_columns = len(other.g[0])
    
        # empty list that will hold the product of self.g x other.g
        mul_mat = []
        row_result = []
    
        for i in range(m_rows):
            row_result = []
            for j in range(p_columns):
                row_A = get_row(self.g, i)
                column_B = get_column(other.g, j)
                result = dot_product(row_A, column_B)
                # append multiplication for each element as a row
                row_result.append(result)
            
            # append each row 
            mul_mat.append(row_result)
            
        return Matrix(mul_mat)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
            #   
            # TODO - your code here
            
            for i in range(len(self.g)):
                for j in range(len(self.g[0])):
                    self.g[i][j] *= other
            return Matrix(self.g)
        else:
            return Matrix(self.g)