import sys
import getopt
import json

import utils

# sys.argv is how you access command line args
# take a slice from 1 to the end so we skip main.py
args = sys.argv[1:]
# extract the filename
filename = args[0]

output = []

# now read the file
with open(filename, "r+") as file:
    contents = json.load(file)

# iterate through all the inputs
# json.load() has converted the json into python data structures
for c in contents:
  alphabet = c["alphabet"]
  row_length = c["rowLength"]
  starting_focus = c["startingFocus"]
  word = c["word"]

  # First create the keyboard
  keyboard = utils.createKeyboard(alphabet, row_length)

  # Now calculate the shortest path
  result = utils.shortestPathOnKeyboard(keyboard, starting_focus, word)
  output.append(result)

print(output)
