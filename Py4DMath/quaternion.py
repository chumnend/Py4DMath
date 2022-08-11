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
  """
  def __init__(self, s: float, v: Vector3D):
    self.s = s
    self.v = v

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
