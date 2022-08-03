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
