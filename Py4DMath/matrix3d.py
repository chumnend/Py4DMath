from __future__ import annotations
from copy import deepcopy

class Matrix3D:
  """
  A class to represent a matrix

  ...
  Attributes
  ----------

  Methods
  ----------
  """

  def __init__(self):
    """
    Constructs all necessary attributes for the Matrix3D object

    Parameters
    ----------
    """
    self.matrix = [0.0]*9

  def __repr__(self) -> str:
    return f"{self.__class__.__name__} (matrix={self.matrix})"

  def copy(self) -> Matrix3D:
    """
    Returns a copy of the matrix.

    Parameters
    ----------
      None

    Returns
    ----------
      (Matrix3D) the copied vector
    """
    return deepcopy(self)
