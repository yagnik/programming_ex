from math import pi

def parse_command(command, rover):
	for token in command.lower():
		if token in __input_map(rover):
			__input_map(rover)[token]()

def parse_setup(inp):
  return map(lambda i: int(i), inp.strip().split(' '))

def parse_location(inp):
  data = inp.strip().split(' ')
  return map(lambda i: int(i), data[:2]) + [parse_direction(data[2])]

def parse_direction(direction):
  return {
    "e" : 0,
    "n" : pi / 2,
    "w" : pi,
    "s" : (2 * pi) / 3
  }[direction.lower()]

def __input_map(rover):
  return {
    'l' : rover.turn_left,
    'r' : rover.turn_right,
    'm' : rover.move
  }
