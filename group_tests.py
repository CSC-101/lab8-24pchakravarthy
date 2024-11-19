import unittest
from group import groups_of_3

class TestGroupsof3(unittest.TestCase):
    def test_1st_groups_of_3(self):
        self.assertEqual(groups_of_3([2, 4, 6, 8, 10, 12, 14, 16, 18]), [[2, 4, 6], [8, 10, 12], [14, 16, 18]])

    def test_2nd_groups_of_3(self):
        self.assertEqual(groups_of_3([2, 4, 6, 8]), [[2, 4, 6], [8]])

    def test_3rd_groups_of_3(self):
        self.assertEqual(groups_of_3([2, 4]), [[2, 4]])

    def test_4th_groups_of_3(self):
        self.assertEqual(groups_of_3([2, 4, 6, 8, 10]), [[2, 4, 6], [8, 10]])