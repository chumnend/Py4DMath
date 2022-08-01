from Py4DMath import Vector3D
from math import sqrt

def test_Vector3D_init_with_no_values():
  v = Vector3D()

  assert v.x == 0.0
  assert v.y == 0.0
  assert v.z == 0.0

def test_Vector3D_init_with_values():
  v = Vector3D(1.0, 2.0, 3.0)

  assert v.x == 1.0
  assert v.y == 2.0
  assert v.z == 3.0

def test_Vector3D_copy():
  v = Vector3D(1, 2, 3)
  copy_v = v.copy()

  assert v.x == copy_v.x
  assert v.y == copy_v.y
  assert v.z == copy_v.z

def test_Vector3D_add_operator():
  v1 = Vector3D(1, 2, 3)
  v2 = Vector3D(4, 5, 6)
  v3 = v1 + v2

  assert v3.x == 5
  assert v3.y == 7
  assert v3.z == 9

def test_Vector3D_add_method():
  v1 = Vector3D(1, 2, 3)
  v2 = Vector3D(4, 5, 6)
  v3 = v1.add(v2)

  assert v3.x == 5
  assert v3.y == 7
  assert v3.z == 9

def test_Vector3D_subtract_operator():
  v1 = Vector3D(1, 2, 3)
  v2 = Vector3D(4, 5, 6)
  v3 = v2 - v1

  assert v3.x == 3
  assert v3.y == 3
  assert v3.z == 3

def test_Vector3D_subtract_method():
  v1 = Vector3D(1, 2, 3)
  v2 = Vector3D(4, 5, 6)
  v3 = v2.subtract(v1)

  assert v3.x == 3
  assert v3.y == 3
  assert v3.z == 3

def test_Vector3D_multiply_operator():
  v1 = Vector3D(1, 2, 3)
  v2 = v1 * 2

  assert v2.x == 2
  assert v2.y == 4
  assert v2.z == 6

def test_Vector3D_multiply_method():
  v1 = Vector3D(1, 2, 3)
  v2 = v1.multiply(2)

  assert v2.x == 2
  assert v2.y == 4
  assert v2.z == 6


def test_Vector3D_divide_operator():
  v1 = Vector3D(4, 6, 8)
  v2 = v1 / 2

  assert v2.x == 2
  assert v2.y == 3
  assert v2.z == 4

def test_Vector3D_divide_method():
  v1 = Vector3D(4, 6, 8)
  v2 = v1.divide(2)

  assert v2.x == 2
  assert v2.y == 3
  assert v2.z == 4

def test_Vector3D_dot():
  v1 = Vector3D(2, 3, 1)
  v2 = Vector3D(1, 2, 0)
  dotProduct = v1.dot(v2)

  assert dotProduct == 8

def test_Vector3D_cross():
  v1 = Vector3D(2, 3, 1)
  v2 = Vector3D(1, 2, 0)
  v3 = v1.cross(v2)

  assert v3.x == -2
  assert v3.y == 1
  assert v3.z == 1

def test_Vector3D_magnitude():
  v1 = Vector3D(2, 3, 1)
  m = v1.magnitude()

  assert m == sqrt(14)

def test_Vector3D_normalize():
  v1 = Vector3D(2, 3, 1)
  n = v1.normalize()

  assert n.x == (1 / sqrt(14)) * 2
  assert n.y == (1 / sqrt(14)) * 3
  assert n.z == (1 / sqrt(14)) * 1
