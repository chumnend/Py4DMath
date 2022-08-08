from Py4DMath import Matrix3D

def test_Matrix3D_init_with_no_values():
  m = Matrix3D()

  assert m.matrix == [0]*9

def test_Matrix3D_init_with_values():
  m = Matrix3D(0, 3, 6, 1, 4, 7, 2, 5, 8)

  assert m.matrix == [0, 1, 2, 3, 4, 5, 6, 7, 8]

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

def test_Matrix3D_multiply_operator_scalar():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  km = m * 2

  assert km.matrix == [4, 4, 10, 6, 2, 6, 2, 8, 4]

def test_Matrix3D_multiply_operator_matrix():
  """
  7  6 3     3 2 1   63 38 28 
  4  2 5  *  5 3 3 = 42 24 15
  10 6 4     4 2 1   76 46 32
  """

  a = Matrix3D(7, 6, 3, 4, 2, 5, 10, 6, 4)
  b = Matrix3D(3, 2, 1, 5, 3, 3, 4, 2, 1)
  c = a * b

  assert c.matrix == [63, 42, 76, 38, 24, 46, 28, 15, 32]

def test_Matrix3D_multiply_method():
  m = Matrix3D(2, 3, 1, 2, 1, 4, 5, 3, 2)
  km = m.multiply(2)

  assert km.matrix == [4, 4, 10, 6, 2, 6, 2, 8, 4]
