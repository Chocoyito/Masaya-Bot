import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_test1(self):
      self.assertEquals(add(1, 2), 3)

