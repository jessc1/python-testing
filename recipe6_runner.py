from recipe6 import *
import unittest
if __name__ == "__main__":
    for suite_func in [high_and_low, combos, all]:
        print ("Running test suite '%s'" % suite_func.__name__)
        suite = suite_func()
        unittest.TextTestRunner(verbosity=2).run(suite)
