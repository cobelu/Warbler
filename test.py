import unittest


class BasicPerformanceTest(unittest.TestCase):
    def test_basic_performance(self):
        self.assertEqual(True, False)  # add assertion here
        w_s, w_bhp = 0, 0
        ratio = w_s * w_bhp
        self.assertLess(ratio, 400, "Takeoff performance will not be desirable")


if __name__ == '__main__':
    unittest.main()
