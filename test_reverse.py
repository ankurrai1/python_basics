# test file for sleep_in Under TDD concept

import unittest
import nptel

class TestOfWarmupOne(unittest.TestCase):

#=================================================================================> sleep_in
    def test_reverse_no_as_positive_integer(self):
        result = nptel.intreverse(368)
        self.assertEqual(result,863)
    def test_reverse_with_any_random_no_1(self):
        result = nptel.intreverse(4)
        self.assertEqual(result,4)
    def test_reverse_with_any_random_no_2(self):
        result = nptel.intreverse(1234567)
        self.assertEqual(result,7654321)
    def test_reverse_with_any_random_no_3(self):
        result = nptel.intreverse(000)
        self.assertEqual(result,000)


# RUN THE TEST 
if __name__ == "__main__":
    unittest.main()
