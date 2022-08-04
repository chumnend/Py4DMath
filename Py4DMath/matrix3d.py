from __future__ import annotations
from copy import deepcopy

class Matrix3D:
  """
  A class to represent a 3x3 matrix.

  ...
  Attributes
  ----------
    matrix: float[9]
      the array representing the matrix (column-major format)

  Methods
  ----------
    copy():
      Returns a copy of the matrix
    show():
      Prints visual representation of matrix
    add():
      Returns the result of matrix addition.
    subtract():
      Returns the result of matrix subtraction.    
  """

  def __init__(self, m0: float = 0, m3: float = 0, m6: float = 0, m1: float = 0, m4: float = 0, m7: float = 0, m2: float = 0, m5: float = 0, m8: float = 0):
    """
    Constructs all necessary attributes for the Matrix3D object

      0  3  6
      1  4  7
      2  5  8

    Parameters
    ----------
      m0: float
        the value at x=0, y=0
      m3: float
        the value at x=0, y=1
      m6: float
        the value at x=0, y=2
      m1: float
        the value at x=1, y=0
      m4: float
        the value at x=1, y=1
      m7: float
        the value at x=1, y=2
      m2: float
        the value at x=2, y=0
      m5: float
        the value at x=2, y=1
      m8: float
        the value at x=2, y=2

    Returns
    ----------
      None
    """
    self.matrix = [0.0]*9

    self.matrix[0] = m0
    self.matrix[3] = m3
    self.matrix[6] = m6

    self.matrix[1] = m1
    self.matrix[4] = m4
    self.matrix[7] = m7

    self.matrix[2] = m2
    self.matrix[5] = m5
    self.matrix[8] = m8

  def __repr__(self) -> str:
    return f"{self.__class__.__name__} (matrix={self.matrix})"

  def __add__(self, m: Matrix3D) -> Matrix3D:
    return Matrix3D(
      self.matrix[0] + m.matrix[0],
      self.matrix[3] + m.matrix[3],
      self.matrix[6] + m.matrix[6],
      self.matrix[1] + m.matrix[1],
      self.matrix[4] + m.matrix[4],
      self.matrix[7] + m.matrix[7],
      self.matrix[2] + m.matrix[2],
      self.matrix[5] + m.matrix[5],
      self.matrix[8] + m.matrix[8],
    )

  def __sub__(self, m: Matrix3D) -> Matrix3D:
    return Matrix3D(
      self.matrix[0] - m.matrix[0],
      self.matrix[3] - m.matrix[3],
      self.matrix[6] - m.matrix[6],
      self.matrix[1] - m.matrix[1],
      self.matrix[4] - m.matrix[4],
      self.matrix[7] - m.matrix[7],
      self.matrix[2] - m.matrix[2],
      self.matrix[5] - m.matrix[5],
      self.matrix[8] - m.matrix[8],
    )

  def copy(self) -> Matrix3D:
    """
    Returns a copy of the matrix.

    Parameters
    ----------
      None

    Returns
    ----------
      (Matrix3D) the copied matrix
    """
    return deepcopy(self)

  def show(self) -> None:
    """
    Prints the matrix in 3x3 grid.

    Parameters
    ----------
      None

    Returns
    ----------
      None
    """

    print(f"[{self.matrix[0]} {self.matrix[3]} {self.matrix[6]}]")
    print(f"[{self.matrix[1]} {self.matrix[4]} {self.matrix[7]}]")
    print(f"[{self.matrix[2]} {self.matrix[5]} {self.matrix[8]}]")

  def add(self, m: Matrix3D) -> Matrix3D:
    """
    Returns the result of matrix addition.

    Parameters
    ----------
      m: Matrix3D
        the matrix to be added 

    Returns
    ----------
      (Matrix3D) the resulting matrix
    """
    return Matrix3D(
      self.matrix[0] + m.matrix[0],
      self.matrix[3] + m.matrix[3],
      self.matrix[6] + m.matrix[6],
      self.matrix[1] + m.matrix[1],
      self.matrix[4] + m.matrix[4],
      self.matrix[7] + m.matrix[7],
      self.matrix[2] + m.matrix[2],
      self.matrix[5] + m.matrix[5],
      self.matrix[8] + m.matrix[8],
    )

  def subtract(self, m: Matrix3D) -> Matrix3D:
    """
    Returns the result of matrix subtraction.

    Parameters
    ----------
      m: Matrix3D
        the matrix to be subtracted

    Returns
    ----------
      (Matrix3D) the resulting matrix
    """
    return Matrix3D(
      self.matrix[0] - m.matrix[0],
      self.matrix[3] - m.matrix[3],
      self.matrix[6] - m.matrix[6],
      self.matrix[1] - m.matrix[1],
      self.matrix[4] - m.matrix[4],
      self.matrix[7] - m.matrix[7],
      self.matrix[2] - m.matrix[2],
      self.matrix[5] - m.matrix[5],
      self.matrix[8] - m.matrix[8],
    )
