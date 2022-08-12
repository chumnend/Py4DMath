from __future__ import annotations
from copy import deepcopy

from .vector3d import Vector3D

class Quaternion:
  """
  A class representing a Quaternion.

  q = s + v

  where s is a scalar number, v is a vector representing an axis

  ...
  Attributes
  ----------
    s: float
      the scalar number
    v: Vector3D
      the vector representing an axis

  Methods
  ----------
    copy():
      Returns a copy of the quaternion.
    add():
      Returns the result of quaternion addition.
    subtract():
      Returns the result of quaternion subtraction.
  """
  def __init__(self, s: float, v: Vector3D):
    self.s = s
    self.v = v

  def __add__(self, q: Quaternion) -> Quaternion:
    return Quaternion(self.s + q.s, self.v + q.v)

  def __sub__(self, q: Quaternion) -> Quaternion:
    return Quaternion(self.s - q.s, self.v - q.v)

  def copy(self) -> Quaternion:
    """
    Returns a copy of the quaternion.

    Parameters
    ----------
      None

    Returns
    ----------
      (Quaternion) the copied quaternion
    """
    return deepcopy(self)

  def add(self, q: Quaternion) -> Quaternion:
    """
    Returns the result of quaternion addition.

    qa + qb = (sa + sa) + (va + vb) 

    Parameters
    ----------
      q: Quaternion
        the quaternion to be added 

    Returns
    ----------
      (Quaternion) the resulting quaternion
    """
    return Quaternion(self.s + q.s, self.v + q.v)

  def subtract(self, q: Quaternion) -> Quaternion:
    """
    Returns the result of quaternion subtraction.

    Parameters
    ----------
      q: Quaternion
        the quaternion to be subtracted

    Returns
    ----------
      (Quaternion) the resulting quaternion
    """
    return Quaternion(self.s - q.s, self.v - q.v)
