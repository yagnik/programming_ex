import os, sys
from rovers import MarsRover
from io import parser
from tests import test_runner

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

def run_main():
  coordinates = parser.parse_setup(raw_input('Enter top right coordinates:\n'))
  while 1:
    location = parser.parse_location(raw_input('Enter rover location:\n'))
    rover = MarsRover(*(coordinates+location))
    parser.parse_command(raw_input('Enter command:\n'), rover)
    print rover.get_position()

if(len(sys.argv) > 1 and (sys.argv[1].lower() in ['-t', '-test', '--t', '--test'])):
  test_runner.run()
else:
  run_main()
