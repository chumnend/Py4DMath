from Py4DMath import Matrix3D

def test_Matrix3D_init():
  m = Matrix3D()

  assert m.matrix == [0]*9


def test_Matrix3D_copy():
  m1 = Matrix3D()
  m2 = m1.copy()

  assert m2.matrix == [0]*9
