from Py4DMath import Quaternion, Vector3D

def test_Quaternion_init():
  v = Vector3D(1, 0, 0)
  q = Quaternion(90, v)

  assert q.s == 90
  assert q.v.x == 1
  assert q.v.y == 0
  assert q.v.z == 0

def test_Quaternion_copy():
  v = Vector3D(1, 0, 0)
  q = Quaternion(90, v)
  q_copy = q.copy()

  assert q_copy.s == 90
  assert q_copy.v.x == 1
  assert q_copy.v.y == 0
  assert q_copy.v.z == 0
