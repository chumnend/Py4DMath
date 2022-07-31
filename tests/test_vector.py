from Py4DMath import Vector

def test_Vector_initialized_with_no_values():
  v = Vector()
  assert v.x == 0.0
  assert v.y == 0.0
  assert v.z == 0.0

def test_Vector_initialized_with_values():
  v = Vector(1.0, 2.0, 3.0)
  assert v.x == 1.0
  assert v.y == 2.0
  assert v.z == 3.0
