import unittest
from math import pi
from rovers import MarsRover

class MarsRoverTest(unittest.TestCase):
	def test_distance(self):
		self.assertEqual(MarsRover.DISTANCE, 1)

	def test_circle_angle(self):
		self.assertEqual(MarsRover.COMPLETE_CIRCLE, (2 * pi))

	def test_initialization_without_params(self):
		rover = MarsRover()
		self.assertEqual(rover.angle, 0)
		self.assertEqual(rover.x_pos, 0)
		self.assertEqual(rover.y_pos, 0)
		self.assertEqual(rover.x_length, 0)
		self.assertEqual(rover.y_length, 0)

	def test_initialization_with_params(self):
		rover = MarsRover(1, 1, 1, 2, 3)
		self.assertEqual(rover.angle, 3)
		self.assertEqual(rover.x_pos, 1)
		self.assertEqual(rover.y_pos, 2)
		self.assertEqual(rover.x_length, 1)
		self.assertEqual(rover.y_length, 1)

	def test_move(self):
		rover = MarsRover()
		rover.move()
		self.assertEqual(rover.x_pos, 1)
		self.assertEqual(rover.y_pos, 0)

	def test_turn_left(self):
		rover = MarsRover()
		rover.turn_left()
		self.assertEqual(rover.angle, pi/2)
		rover.turn_left()
		self.assertEqual(rover.angle, pi)
		rover.turn_left()
		rover.turn_left()
		self.assertEqual(rover.angle, 0)

	def test_turn_right(self):
		rover = MarsRover()
		rover.turn_right()
		self.assertEqual(rover.angle, 3*pi/2)
		rover.turn_right()
		self.assertEqual(rover.angle, pi)
		rover.turn_right()
		rover.turn_right()
		self.assertEqual(rover.angle, 0)

	def test_turn_angle(self):
		rover = MarsRover()
		rover.turn(5)
		self.assertEqual(rover.angle, 5)

	def test_turn_angle_more_than_2pi(self):
		rover = MarsRover()
		rover.turn(3*pi)
		self.assertEqual(rover.angle, pi)

	def test_get_position(self):
		rover = MarsRover()
		self.assertEqual(rover.get_position(), "0 0 E")

