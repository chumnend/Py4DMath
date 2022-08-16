import pytest

from Py4DMath import Quaternion, Vector3D
from math import sqrt

def test_Quaternion_getRotationQuaternion():
  q_r = Quaternion.getRotationQuaternion(90, Vector3D(1, 0, 0))

  assert round(q_r.s, 6) == 0.707107
  assert round(q_r.v.x, 6) == 0.707107
  assert round(q_r.v.y, 6) == 0
  assert round(q_r.v.z, 6) == 0

def test_Quaternion_init():
  v = Vector3D(1, 0, 0)
  q = Quaternion(90, v)

  assert q.s == 90
  assert q.v.x == 1
  assert q.v.y == 0
  assert q.v.z == 0

def test_Quaternion_repr():
  v = Vector3D(1, 0, 0)
  q = Quaternion(90, v)

  assert repr(q) == "Quaternion (quaternion=90 + 1i + 0j + 0k)"

def test_Quaternion_copy():
  v = Vector3D(1, 0, 0)
  q = Quaternion(90, v)
  q_copy = q.copy()

  assert q_copy.s == 90
  assert q_copy.v.x == 1
  assert q_copy.v.y == 0
  assert q_copy.v.z == 0

def test_Quaternion_add_operator():
  a = Quaternion(0.5, Vector3D(2, 3, -4))
  b = Quaternion(0.1, Vector3D(4, 5, 6))
  c = a + b

  assert c.s == 0.6
  assert c.v.x == 6
  assert c.v.y == 8
  assert c.v.z == 2

def test_Quaternion_add():
  a = Quaternion(0.5, Vector3D(2, 3, -4))
  b = Quaternion(0.1, Vector3D(4, 5, 6))
  c = a.add(b)

  assert c.s == 0.6
  assert c.v.x == 6
  assert c.v.y == 8
  assert c.v.z == 2

def test_Quaternion_sub_operator():
  a = Quaternion(0.5, Vector3D(2, 3, -4))
  b = Quaternion(0.1, Vector3D(4, 5, 6))
  c = a - b

  assert c.s == 0.4
  assert c.v.x == -2
  assert c.v.y == -2
  assert c.v.z == -10

def test_Quaternion_subtract():
  a = Quaternion(0.5, Vector3D(2, 3, -4))
  b = Quaternion(0.1, Vector3D(4, 5, 6))
  c = a.subtract(b)

  assert c.s == 0.4
  assert c.v.x == -2
  assert c.v.y == -2
  assert c.v.z == -10

def test_Quaternion_mul_operator():
  a = Quaternion(90, Vector3D(1, 0 , 0))
  b = a * 2

  assert b.s == 180
  assert b.v.x == 2
  assert b.v.y == 0
  assert b.v.z == 0

  d = Quaternion(90, Vector3D(1, 0 , 0))
  e = Quaternion(10, Vector3D(1, 0 ,0))
  f = d * e

  assert f.s == 899
  assert f.v.x == 100
  assert f.v.y == 0
  assert f.v.z == 0

def test_Quaternion_mul_error():
  with pytest.raises(Exception):
    v = Vector3D(1, 0, 0)
    q = Quaternion(90, v)
    res = q * "hello"

def test_Quaternion_scalar_multiply():
  a = Quaternion(90, Vector3D(1, 0 , 0))
  b = a.scalar_multiply(2)

  assert b.s == 180
  assert b.v.x == 2
  assert b.v.y == 0
  assert b.v.z == 0


def test_Quaternion_quaternion_multiply():
  a = Quaternion(90, Vector3D(1, 0 , 0))
  b = Quaternion(10, Vector3D(1, 0 ,0))
  c = a.quaternion_multiply(b)

  assert c.s == 899
  assert c.v.x == 100
  assert c.v.y == 0
  assert c.v.z == 0

def test_Quaternion_norm():
  q = Quaternion(1, Vector3D(2, 3, 4))
  n = q.norm()

  assert n == sqrt(30)

def test_Quaternion_normalize():
  q = Quaternion(1, Vector3D(2, 3, 4))
  n = q.normalize()

  assert n.s == 1 / sqrt(30)
  assert n.v.x == 2 / sqrt(30)
  assert n.v.y == 3 / sqrt(30)
  assert n.v.z == 4 / sqrt(30)

def test_Quaternion_normalize_error():
  with pytest.raises(Exception):
      v = Vector3D(0, 0, 0)
      q = Quaternion(0, v)
      q.normalize()

def test_Quaternion_conjugate():
  q = Quaternion(90, Vector3D(1, 0, 0))
  q_conj = q.conjugate()

  assert q_conj.s == 90
  assert q_conj.v.x == -1
  assert q_conj.v.y == 0
  assert q_conj.v.z == 0

def test_Quaternion_inverse():
  q = Quaternion(60, Vector3D(1, 0, 0))
  q_inv = q.inverse()

  assert q_inv.s == 0.016662038322688144 
  assert q_inv.v.x == -0.00027770063871146905
  assert q_inv.v.y == 0
  assert q_inv.v.z == 0
