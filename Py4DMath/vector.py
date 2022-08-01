from __future__ import annotations
from copy import deepcopy
from math import sqrt

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

  def __mul__(self, k: float) -> Vector3D:
    return Vector3D(
      k * self.x,
      k * self.y,
      k * self.z,
    )

  def __truediv__(self, k: float) -> Vector3D:
    return Vector3D(
      self.x / k,
      self.y / k,
      self.z / k,
    )

  def copy(self) -> Vector3D: 
    return deepcopy(self)

  def add(self, v: Vector3D) -> Vector3D:
    return Vector3D(
      self.x + v.x,
      self.y + v.y,
      self.z + v.z,
    )

  def subtract(self, v:  Vector3D) -> Vector3D:
    return Vector3D(
      self.x - v.x,
      self.y - v.y,
      self.z - v.z,
    )

  def multiply(self, k: float) -> Vector3D:
    return Vector3D(
      k * self.x,
      k * self.y,
      k * self.z,
    )

  def divide(self, k: float) -> Vector3D:
    return Vector3D(
      self.x / k,
      self.y / k,
      self.z / k,
    )

  def dot(self, v: Vector3D) -> float:
    return self.x * v.x + self.y * v.y + self.x * v.z

  def cross(self, v: Vector3D) -> Vector3D:
    return Vector3D(
      self.y * v.z - self.z * v.y,
      self.z * v.x - self.x * v.z,
      self.x * v.y - self.y * v.x,
    )

  def magnitude(self) -> float:
    return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

  def normalize(self) -> Vector3D:
    m = self.magnitude()

    if (m > 0.0):
      factor = 1.0 / m
      return Vector3D(
        factor * self.x,
        factor * self.y,
        factor * self.z,
      )
    else:
      return Vector3D()
