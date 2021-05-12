import altimetrik
import unittest
import pandas as pd
import numpy as np


class Test(unittest.TestCase):

	def test_check_age(self):
		self.age = 15
		self.assertEqual(altimetrik.check_age(self.age), "kids")
		self.age1 = 19
		self.assertEqual(altimetrik.check_age(self.age1), "Adults")
		self.age2 = 63
		self.assertEqual(altimetrik.check_age(self.age2), "Elders")
		self.age3 = np.nan
		self.assertEqual(altimetrik.check_age(self.age3), "Couldn't determine the age group")

	def test_class_selection(self):
		self.cabin = 'C180'
		self.assertEqual(altimetrik.class_selection(self.cabin), 'First Class')
		self.cabin = 'S017'
		self.assertEqual(altimetrik.class_selection(self.cabin), 'Second Class')
		self.cabin = np.nan
		self.assertEqual(altimetrik.class_selection(self.cabin), 'Not mentioned')

	def test_gender(self):
		self.name = "Braund, Mr. Owen Harris"
		self.assertEqual(altimetrik.gender(self.name), 'Male')
		self.name = "Heikkinen, Miss. Laina"
		self.assertEqual(altimetrik.gender(self.name), 'Female')
		self.name = "Nasser, Mrs. Nicholas (Adele Achem)"
		self.assertEqual(altimetrik.gender(self.name), 'Female')


if __name__ == '__main__':
	unittest.main()
	