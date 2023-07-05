import unittest
from fuel import convert, gauge

class FuelTestCase(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert("0/4"), 0)
        self.assertEqual(convert("1/100"), 1)
        self.assertEqual(convert("3/4"), 75)
        self.assertEqual(convert("1/4"), 25)
        self.assertEqual(convert("99/100"), 99)

        with self.assertRaises(ZeroDivisionError):
            convert("1/0")

        with self.assertRaises(ValueError):
            convert("cat/dog")

    def test_gauge(self):
        self.assertEqual(gauge(0), "E")
        self.assertEqual(gauge(75), "75%")
        self.assertEqual(gauge(25), "25%")
        self.assertEqual(gauge(99), "F")
        self.assertEqual(gauge(1), "E")

if __name__ == '__main__':
    unittest.main()
