class Node:
  # parent is another node
  parent = None
  # value is a number
  value = None
  # path is a list of how to get here
  path = None

  def __init__(self, parent, value, path):
    self.parent = parent
    self.value = value
    self.path = path
