class Vector:
  def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f"{self.__class__.__name__} (x={self.x} y={self.y} z={self.z})"
