from __future__ import annotations
from copy import deepcopy

class Vector3D:
  def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self) -> str:
    return f"{self.__class__.__name__} (x={self.x} y={self.y} z={self.z})"

  def __add__(self, v: Vector3D) -> Vector3D:
    return Vector3D(
      self.x + v.x,
      self.y + v.y,
      self.z + v.z,
    )

  def __sub__(self, v:  Vector3D) -> Vector3D:
    return Vector3D(
      self.x - v.x,
      self.y - v.y,
      self.z - v.z,
    )

  def copy(self) -> Vector3D: 
    return deepcopy(self)
