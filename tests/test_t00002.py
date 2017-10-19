import unittest

func_to_test = 'sum_array'
sum_array = lambda: None

class TestArraySum(unittest.TestCase):
	def test_empty(self):
		self.assertEqual(sum_array([]), 0)

	def test_one_element(self):
		for i in range(-1,2):
			with self.subTest(i=i):
				self.assertEqual(sum_array([i]), 0)

	def test_two_elements(self):
		with self.subTest():
			self.assertEqual(sum_array([ 3, 5]), 0)
			self.assertEqual(sum_array([-3, -5]), 0)

	def test_else(self):
		with self.subTest():
			self.assertEqual(sum_array([6, 2, 1, 8, 10]), 16)
			self.assertEqual(sum_array([6, 0, 1, 10, 10]), 17)
			self.assertEqual(sum_array([-6, -20, -1, -10, -12]), -28)
			self.assertEqual(sum_array([-6, 20, -1, 10, -12]), 3)
