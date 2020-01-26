from node import Node

def createKeyboard(alphabet, row_length):
  # dictionary for fast lookup of locations
  lookup = {}
  # use a list to hold the actual graph
  graph = []
  # use a list to hold each row of the keyboard
  row = []
  # keep track of the x,y coordinates of each letter
  x = 0
  y = 0

  # time to build the keyboard
  for index, letter in enumerate(alphabet):

    if index != 0 and index % row_length == 0:
      x = 0
      y += 1
      graph.append(row)
      row = []

    lookup[letter] = [x,y]
    row.append(letter)
    x += 1

  # Don't forget the last row
  graph.append(row)

  # return the lookup table and the graph we've built
  return (lookup, graph)

def shortestPathOnKeyboard(keyboard, starting_focus, word):
  distance = 0
  path = []
  start = starting_focus

  for letter in word:
    # Find the target node
    target = breadthFirstSearch(start, letter, keyboard)
    start = letter

    # trace back from the end to the start
    node = target
    newPath = []


  return (distance, path)

def breadthFirstSearch(start, end, keyboard):
  # use a list as our queue thanks to append() and pop()
  queue = []

  # create a dictionary to record all the nodes we've seen
  discovered = {}

  lookup = keyboard[0]
  graph = keyboard[1]

  n = Node(None, 7, [])
  return n
