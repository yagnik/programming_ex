from math import sin, cos, pi

class MarsRover:
  COMPLETE_CIRCLE = (2 * pi)
  DISTANCE = 1

  def __init__(self, x_length=0, y_length=0, x_pos=0, y_pos=0, angle=0):
    self.angle = angle
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.x_length = x_length
    self.y_length = y_length

  def move(self):
    self.x_pos = self.x_pos + (self.DISTANCE * cos(self.angle))
    self.y_pos = self.y_pos + (self.DISTANCE * sin(self.angle))

  def turn(self, angle):
    self.angle = (self.angle + angle) % self.COMPLETE_CIRCLE

  def turn_left(self):
    self.turn(pi / 2)

  def turn_right(self):
    self.turn(-pi / 2)

  def get_position(self):
    return "{0} {1} {2}".format((int(self.x_pos)), (int(self.y_pos)), self.__get_direction())

  def __get_direction(self):
    return {
      0        : "E",
      pi/2     : "N",
      pi       : "W",
      (2*pi/3) : "S"
    }[self.angle]