import pytest

from Py4DMath import Matrix3D, Vector3D

def test_Matrix3D_getIdentityMatrix():
  m = Matrix3D.getIdentityMatrix()

  assert m.matrix == [1, 0, 0, 0, 1, 0, 0, 0, 1]

def test_Matrix3D_init_with_no_values():
  m = Matrix3D()

  assert m.matrix == [0]*9

def test_Matrix3D_init_with_values_column_major():
  m = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8, major="column")

  assert m.matrix == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_Matrix3D_init_with_values_row_major():
  m = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8, major="row")

  assert m.matrix == [0, 3, 6, 1, 4, 7, 2, 5, 8]

def test_Matrix3D_init_major_error():
  with pytest.raises(Exception):
    m = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8, major="test")

def test_Matrix3D_repr_():
    m = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8, major="column")

    assert repr(m) == "Matrix3D (matrix=[0, 1, 2, 3, 4, 5, 6, 7, 8])"

def test_Matrix3D_copy():
  m1 = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8)
  m2 = m1.copy()

  assert m2.matrix == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_Matrix3D_add_operator():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  n = Matrix3D(5, 3, 2, 2, 1, 1, 5, 3, 2)

  mn = m + n

  assert mn.matrix == [7, 4, 10, 6, 2, 6, 3, 5, 4]

def test_Matrix3D_add_method():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  n = Matrix3D(5, 3, 2, 2, 1, 1, 5, 3, 2)

  mn = m.add(n)

  assert mn.matrix == [7, 4, 10, 6, 2, 6, 3, 5, 4]

def test_Matrix3D_sub_operator():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  n = Matrix3D(5, 3, 2, 2, 1, 1, 5, 3, 2)

  mn = m - n

  assert mn.matrix == [-3, 0, 0, 0, 0, 0, -1, 3, 0]

def test_Matrix3D_sub_method():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  n = Matrix3D(5, 3, 2, 2, 1, 1, 5, 3, 2)

  mn = m.subtract(n)

  assert mn.matrix == [-3, 0, 0, 0, 0, 0, -1, 3, 0]

def test_Matrix3D_mul_scalar():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  km = m * 2

  assert km.matrix == [4, 4, 10, 6, 2, 6, 2, 8, 4]

def test_Matrix3D_mul_matrix():
  a = Matrix3D(7, 6, 3, 4, 2, 5, 10, 6, 4)
  b = Matrix3D(3, 2, 1, 5, 3, 3, 4, 2, 1)
  c = a * b

  assert c.matrix == [63, 42, 76, 38, 24, 46, 28, 15, 32]

def test_Matrix3D_mul_vector():
  m = Matrix3D(0, 0, 0, 0, 0 ,-1, 0, 1, 0)
  v = Vector3D(0, 1, 0)
  r = m * v

  assert r.x == 0
  assert r.y == 0
  assert r.z == 1

def test_Matrix3D_mul_error():
  with pytest.raises(Exception):
      m = Matrix3D(0, 0, 0, 0, 0 ,-1, 0, 1, 0)
      r = m * "test"

def test_Matrix3D_scalar_multiply():
  a = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  b = a.scalar_multiply(2)

  assert b.matrix == [4, 4, 10, 6, 2, 6, 2, 8, 4]

def test_Matrix3D_matrix_multiply():
  a = Matrix3D(7, 6, 3, 4, 2, 5, 10, 6, 4)
  b = Matrix3D(3, 2, 1, 5, 3, 3, 4, 2, 1)
  c = a.matrix_multiply(b)

  assert c.matrix == [63, 42, 76, 38, 24, 46, 28, 15, 32]

def test_inverse():
  """
      2 1 4           -1/5  -1/5  1
  M = 3 4 1    M^-1 =  1/15  2/5 -2/3
      2 1 1            1/3   0   -1/3
  """
  m = Matrix3D(2, 3, 2, 1, 4, 1, 4, 1, 1)
  m_inv = m.inverse()

  assert m_inv.matrix == [-1/5, 1/15, 1/3, -1/5, 2/5, 0, 1, -2/3, -1/3]

def test_inverse_error():
  m = Matrix3D(-5, 0 , 2, 1, -2, 3, 6, -2, 1, major="row") 
  assert m.inverse() == None

def test_transpose():
  m = Matrix3D(2, 1, 4, 3, 4, 1, 2, 1, 1)
  m_trans = m.transpose()

  assert m_trans.matrix == [2, 1, 4, 3, 4, 1, 2, 1, 1]

def test_transform():
  m = Matrix3D(0, 0, 0, 0, 0 ,-1, 0, 1, 0)
  v = Vector3D(0, 1, 0)

  r = m.transform(v)

  assert r.x == 0
  assert r.y == 0
  assert r.z == 1
