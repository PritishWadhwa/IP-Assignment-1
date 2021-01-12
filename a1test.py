# Name : PRITISH WADHWA
# Roll No : 2019440
# Group : 1


import unittest
from a1 import changeBase


# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):

    def test_change_base(self):
        self.assertAlmostEqual(changeBase(67, "INR", "GBP", "2010-10-10"), 0.951, delta=0.001)
        self.assertEqual(changeBase(75, "CAD", "EEK", "2000-01-01"), 803.3235213581598)
        self.assertGreaterEqual(changeBase(182, "PHP", "TRY", "2011-11-11"), 7)
        self.assertLessEqual(changeBase(1131231, "PLN", "AUD", "2019-01-19"), 420000)
        self.assertNotEqual(changeBase(0.001212, "LVL", "SIT", "1999-01-04"), 1.23)
    # these are just sample values. You have to add testcases (and edit these) for various dates.
    # (don't use the current date as the json would keep changing every 4 minutes)
    # you have to hard-code the 2nd parameter of assertEquals by calculating it manually
    # on a particular date and checking whether your changeBase function returns the same
    # value or not.


if __name__ == '__main__':
    unittest.main()
