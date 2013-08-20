import unittest
from io import parser
from rovers import MarsRover

class ParserTest(unittest.TestCase):
  def test_parse_command(self):
    rover = MarsRover()
    parser.parse_command("m", rover)
    self.assertEqual(rover.get_position(), "1 0 E")
    parser.parse_command("x", rover)
    self.assertEqual(rover.get_position(), "1 0 E")
    parser.parse_command("l", rover)
    self.assertEqual(rover.get_position(), "1 0 N")
    parser.parse_command("r", rover)
    self.assertEqual(rover.get_position(), "1 0 E")

  def test_parse_setup(self):
    self.assertEqual(parser.parse_setup(" 2 2 "), [2, 2])
    self.assertRaises(Exception, parser.parse_setup, " 2 x")

  def test_parse_location(self):
    self.assertEqual(parser.parse_location(" 2 2 e "), [2, 2, 0])

  def test_parse_direction(self):
    self.assertEqual(parser.parse_direction("E"),0)
    self.assertEqual(parser.parse_direction("e"),0)
    self.assertRaises(Exception, parser.parse_direction, "x")
