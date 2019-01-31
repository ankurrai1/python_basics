# test file for sleep_in Under TDD concept

import unittest
import warmup_one

class TestOfWarmupOne(unittest.TestCase):

#=================================================================================> sleep_in
    def test_sleep_in_With_weekday_vacation__as_false_false(self):
        result = warmup_one.sleep_in(False,False)
        self.assertTrue(result)
    def test_sleep_in_With_weekday_vacation__as_false_true(self):
        result = warmup_one.sleep_in(False,True)
        self.assertTrue(result)
    def test_sleep_in_With_weekday_vacation__as_true_false(self):
        result = warmup_one.sleep_in(True,False)
        self.assertFalse(result)
    def test_sleep_in_With_weekday_vacation__as_true_true(self):
        result = warmup_one.sleep_in(True,True)
        self.assertTrue(result)

#=================================================================================>


# RUN THE TEST 
if __name__ == "__main__":
    unittest.main()