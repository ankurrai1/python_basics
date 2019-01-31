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

#=================================================================================> monkey_trouble

    def test_monkey_trouble_With_a_smile_b_smile_as_false_false(self):
        result = warmup_one.monkey_trouble(False,False)
        self.assertTrue(result)
    def test_monkey_trouble_With_a_smile_b_smile_as_false_true(self):
        result = warmup_one.monkey_trouble(False,True)
        self.assertFalse(result)
    def test_monkey_trouble_With_a_smile_b_smile_as_true_false(self):
        result = warmup_one.monkey_trouble(True,False)
        self.assertFalse(result)
    def test_monkey_trouble_With_a_smile_b_smile_as_true_true(self):
        result = warmup_one.monkey_trouble(True,True)
        self.assertTrue(result)
#======================================================================================>sum_double

    def test_sum_double_With_integers_3_4(self):
        result = warmup_one.sum_double(3,4)
        self.assertEqual(result,7)
    def test_sum_double_With_integers_4_4(self):
        result = warmup_one.sum_double(4,4)
        self.assertEqual(result,16)
    def test_sum_double_With_integers_3_1(self):
        result = warmup_one.sum_double(3,1)
        self.assertEqual(result,4)
    def test_sum_double_With_integers_0_0(self):
        result = warmup_one.sum_double(0,0)
        self.assertEqual(result,0)





# RUN THE TEST 
if __name__ == "__main__":
    unittest.main()