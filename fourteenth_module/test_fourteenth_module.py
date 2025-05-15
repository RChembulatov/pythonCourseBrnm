import unittest
from fourteenth_module import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr), sorted(arr))

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(merge_sort(arr), sorted(arr))

    def test_random_array(self):
        arr = [3, 1, 4, 1, 5, -9, 2, 6, -5, 3, 5]
        self.assertEqual(merge_sort(arr), sorted(arr))


unittest.main()
