from Py4DMath import Vector3D

def test_Vector3D_initialized_with_no_values():
  v = Vector3D()
  assert v.x == 0.0
  assert v.y == 0.0
  assert v.z == 0.0

def test_Vector3D_initialized_with_values():
  v = Vector3D(1.0, 2.0, 3.0)
  assert v.x == 1.0
  assert v.y == 2.0
  assert v.z == 3.0
