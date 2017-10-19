import unittest

func_to_test = 'year_days'
year_days = lambda: None

class TestLeapYearFunction(unittest.TestCase):

	def test_isleap(self):
		for i in range(0, 120, 4):
			with self.subTest(i=i):
				if i % 100 != 0:
					self.assertEqual(year_days(i), "{} has 366 days".format(i))					

	def test_notleap(self):
		for i in range(0, 120, 3):
			with self.subTest(i=i):
				if i % 4 != 0:
					self.assertEqual(year_days(i), "{} has 365 days".format(i))
					
	def test_centuriesleap(self):
		for i in range(-500, 500, 100):
			with self.subTest(i=i):
				if i % 400 == 0:
					self.assertEqual(year_days(i), "{} has 366 days".format(i))

	def test_cenuries_notleap(self):
		for i in range(-500, 500, 100):
			with self.subTest(i=i):
				if i % 400 != 0:
					self.assertEqual(year_days(i), "{} has 365 days".format(i))

	def test_negative_notleap(self):
		for i in range(-120, 0, 3):
			with self.subTest(i=i):
				if i % 4 != 0:
					self.assertEqual(year_days(i), "{} has 365 days".format(i))

	def test_zeroyear(self):
		self.assertEqual(year_days(0), "0 has 366 days")

	def test_negative_leap(self):
		for i in range(-12, 0, 4):
			with self.subTest(i=i):
				if i % 100 != 0:
					self.assertEqual(year_days(i), "{} has 366 days".format(i))