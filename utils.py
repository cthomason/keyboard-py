from node import Node
from neighbour import Neighbour

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

  # extract the lookup table and graph from the keyboard
  lookup = keyboard[0]
  graph = keyboard[1]

  # construct the starting node
  start_node = Node(None, start, None)

  # Mark the first node as discovered
  discovered[start] = True

  # Add the first node to the queue
  queue.append(start_node)

  # Keep going until the queue is empty
  while len(queue) > 0:
    r = shift(queue)
    current_node = r[0]
    queue = r[1]

    # if it's the one we're looking for then return
    if current_node.value == end:
      return current_node

    # retrieve the location of the current node
    location = lookup[current_node.value]

    # this is the origin
    x = location[0]
    y = location[1]

    neighbours = [
      Neighbour(x, y - 1, "u"),
      Neighbour(x, y + 1, "d"),
      Neighbour(x - 1, y, "l"),
      Neighbour(x + 1, y, "r")
    ]

    # calculate the number of columns to wrap around the cursor
    num_cols = len(graph[y])
    num_rows = len(graph)


# while (!graph[numRows - 1] || !graph[numRows - 1][x]) {
#       numRows -= 1;
#     }
    # since the keyboard is left aligned we may need to adjust num_rows
    while num_rows >= 0:
      num_rows -= 1

    # now visit each neighbour
    for neighbour in neighbours:
      x1 = neighbour.x
      y1 = neighbour.y

      # wrap around if needed
      if y1 < 0:
        y1 += num_rows
      else:
        # we can safely use the modulo operator here because it will return the
        # original value of y1
        y1 %= num_rows

      # wrap around if needed
      if x1 < 0:
        x1 += num_cols
      else:
        x1 %= num_cols

      # construct a new node object
      node = Node(current_node, graph[y1][x1], neighbour.direction)

      # only add undiscovered nodes to the queue
      if node.value not in discovered:
        discovered[node.value] = True
        queue.append(node)

def shift(array):
  # use a slice to grab the first element of the array
  element = array[0]

  # then use another slice to grab all remaining elements of the array
  new_array = array[1:]

  # return the values
  return (element, new_array)
