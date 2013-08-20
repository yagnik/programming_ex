import unittest
from rovers.mars_rover import MarsRoverTest
from io.parser import ParserTest

def run():
  __run_suite(unittest.TestLoader().loadTestsFromTestCase(MarsRoverTest))
  __run_suite(unittest.TestLoader().loadTestsFromTestCase(ParserTest))

def __run_suite(suite):
  unittest.TextTestRunner().run(suite)