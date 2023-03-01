import unittest, sys

from rle_program import *


class TestRLEProjectMethods(unittest.TestCase):
    def test_to_hex_string(self):
        self.assertEqual(to_hex_string([3, 15, 6, 4]), "3f64")

    def test_count_runs(self):
        self.assertEqual(count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]), 2)

    def test_count_runs_long(self):
        self.assertEqual(count_runs([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7 ]), 6)

    def test_count_runs_complicated(self):
        self.assertEqual(count_runs([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]), 25)

    def test_encode_rle(self):
        self.assertEqual(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]), [3, 15, 6, 4])

    def test_encode_rle_first(self):
        self.assertEqual(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]), [2,4,15,1,15,1,5,1,1,8,1,7])

    def test_encode_rle_second(self):
        self.assertEqual(encode_rle([1,2,3,4,1,2,3,4]), [1,1,1,2,1,3,1,4,1,1,1,2,1,3,1,4])

    def test_encode_rle_third(self):
        self.assertEqual(encode_rle([4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [2,4,15,1,15,1,5,1])

    def test_encode_rle_fourth(self):
        self.assertEqual(encode_rle([4,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), [1,4,1,5,15,1,15,1,5,1])

    def test_decode_rle(self):
        self.assertEqual(decode_rle([2,4,15,1,15,1,5,1,1,8,1,7]), [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7])

    def test_get_decoded_length(self):
        self.assertEqual(get_decoded_length([3, 15, 6, 4]), 9)

    def test_decode_rle(self):
        self.assertEqual(decode_rle([3, 15, 6, 4]), [15, 15, 15, 4, 4, 4, 4, 4, 4])

    def test_string_to_data(self):
        self.assertEqual(string_to_data("3f64"), [3, 15, 6, 4])


if __name__ == '__main__':
    unittest.main()