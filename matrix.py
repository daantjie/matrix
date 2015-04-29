#!/usr/bin/env python
# Matrix Module
# Daniel Oosthuizen

# {{{=========== MATRIX CLASS ===========
class Matrix:
    """
    Implementation of matrices in python.
    """

# {{{=========== INITIALISE ===============
    def __init__(self, *rows):
        """(list(nums)) -> Matrix

        'Initialise' method. Sets self.rows instance variable, and checks dimensions.
        """
        self.rows = list(rows)
        self.updateDimensions()

    @classmethod
    def Column(class_, *columns):
        """(list(nums)) -> Matrix

        Initialises a matrix instance by column, as opposed to by row.
        """
        for column in columns:
            assert len(column) == len(columns[0]), \
                "Cannot have irregular column length."

        return Matrix(*[list(t) for t in zip(*columns)])
# }}}
# {{{=========== REPRESENTATION ===========
    def __repr__(self):
        """() -> str

        Magic method. Instead of printing <Matrix object at 0x00AF5570>, it gives an actual representation of the matrix.
        """
        maxLen = max([max([len(str(x)) for x in row]) for row in self.rows])
        maxFirstLen = max([len(str(x)) for x in self.column(0)])
        return "\n".join([Matrix.reprList(row, maxLen, maxFirstLen) for row in self.rows])
# }}}
# {{{=========== ACCESSING ================
    def row(self, m):
        """(int) -> list

        Returns row number m of the matrix instance.
        """
        return self.rows[m]


    def column(self, n):
        """(int) -> list

        Returns column number n of the matrix instance.
        """
        return [row[n] for row in self.rows]


    def at(self, i, j):
        """(int, int) -> num

        Returns the value at the coordinates (i, j) of the matrix instance.
        """
        return self.rows[j][i]


    def __getitem__(self, pos):
        """(iter(int, int)) -> num

        Magic method! Alias of 'at'
        """
        return self.at(pos[0], pos[1])
# }}}
# {{{=========== COMPARISON ===============
    def __eq__(self, other):
        """() -> bool

        Magic method! Defines '==' for matrix instances.
        """
        if type(other) == Matrix:
            return self.rows == other.rows
        else:
            return false
# }}}
# {{{=========== COMPUTATION ==============
    def __neg__(self):
        """() -> Matrix

        Magic method! Reverses the sign of the values stored in the matrix instance.
        """
        result = []
        for row in self.rows:
            result.append([-x for x in row])

        return Matrix(*result)


    def __add__(self, other):
        """(Matrix) -> Matrix

        Magic method! Defines '+' for matrix instances.
        """
        assert type(other) == Matrix, \
            "Cannot add a matrix to something that is not a matrix."
        assert (self.m, self.n) == (other.m, other.n), \
            "Cannot add matrices with different dimensions."

        result = []
        for row1, row2 in zip(self.rows, other.rows):
            result.append([sum(x) for x in zip(row1, row2)])
        return Matrix(*result)


    def __sub__(self, other):
        """(Matrix) -> Matrix

        Magic method! Defines '-' for matrix instances.
        """
        return self + (-other)


    def __mul__(self, other):
        """(Matrix) -> Matrix

        Magic method! Defines '*' for matrix instances.
        """
        assert type(other) in (Matrix, Vector, float, int), \
            "Cannot multiply a matrix with something that is not a matrix, vector, or scalar."

        if type(other) in (Matrix, Vector):
            assert self.n == other.m, \
                "Cannot multiply an ?×n matrix by a matrix that is not n×?."

            result = []
            for i in range(self.m):
                row = []
                for j in range(other.n):
                    row.append(sum([x[0]*x[1] for x in zip(self.row(i), other.column(j))]))
                result.append(row)
        else:
            result = [[x*other for x in row] for row in self.rows]
        return Matrix(*result)


    def __rmul__(self, other):
        """(num) -> Matrix

        Magic method! Means 2*M == M*2.
        """
        return self*other


    def augment(self, other):
        """(Matrix) -> Matrix

        Augments the matrix instance with other.
        """
        assert type(other) in (Matrix, Vector), \
                "Cannot augment a matrix with something that is not a matrix or a vector."
        assert self.m == other.m, \
                "Cannot augment a matrix to another matrix/vector that does not have the same number of columns."

        return Matrix(*[x + y for (x, y) in zip(self.rows, other.rows)])


    def reducedRowEchelon(self):
        """() -> Matrix

        Returns the reduced row echelon form of the matrix instance.
        """
        rows = self.rows
        m, n = self.m, self.n
        for i in range(min(m, n)):
            rows[i] = [ x/rows[i][i] for x in rows[i] ]
            for j in range(m):
                if j == i:
                    continue
                rows[j] = [ x - rows[j][i]*y for (x, y) in zip( rows[j], rows[i] ) ]
        return Matrix(*rows)

# }}}
# {{{=========== HELPERS ===================
    def updateDimensions(self):
        """() -> None

        Updates and checks the dimensions of the matrix instance.
        """
        self.m = len(self.rows)
        self.n = len(self.rows[0])
        self.checkDimensions()


    def checkDimensions(self):
        """() -> None

        Checks the dimensions of the matrix instance are correct.
        """
        for row in self.rows:
            assert len(row) == self.n, \
            "Cannot have irregular row length."

    @staticmethod
    def reprList(l, maxLen, maxFirstLen):
        """(list) -> str

        Gives a string representation of a list with proper spacing.
        """
        spacing = [" "*(maxFirstLen - len(str(l[0])))] + [" "*(maxLen - len(str(x))) for x in l[1:len(l)]]
        result = "[" + spacing[0] + str(l[0]) + ","
        for i in range(1, len(l)-1):
            result += spacing[i] + " " + str(l[i]) + ","
        result += spacing[-1] + " " + str(l[-1]) + "]"
        return result
# }}}
# }}}
# {{{=========== VECTOR CLASS =====
class Vector(Matrix):
    """
    Subclass of class Matrix. Initialises an n×1 column matrix, or column vector.
    """
    def __init__(self, *column):
        Matrix.__init__(self, *[[x] for x in column])
# }}}
