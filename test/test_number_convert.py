import unittest

from webfirst import views

class TestNumberConvert(unittest.TestCase):
    def test_to_roman(self):
        data = '1986'
        result = views.arab_to_roman(data)
        self.assertEqual(result, 'MCMLXXXVI')

    def test_negative_arabic(self):
        data = '-1'
        result = views.arab_to_roman(data)
        self.assertEqual(result, '')

    def test_to_arabic(self):
        data = 'MMMCCI'
        result = views.roman_to_arab(data)
        self.assertEqual(result, 3201)

    def test_negative_roman(self):
        data = '-1'
        result = views.roman_to_arab(data)
        self.assertEqual(result, 0)

    def test_any_string(self):
        data = 'SDFGHJKL'
        result = views.roman_to_arab(data)
        self.assertEqual(result, 0)


if __name__ == '__main__':
        unittest.main()
