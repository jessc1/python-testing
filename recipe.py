import unittest

class RomanNUMERALConverter(object):
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.digit_map = { "M":1000, "D":500,"C":100,\
                            "L":50, "X":10, "V":5, "I":1 }

    def convert_to_decimal(self):
        val = 0
        for char in self.roman_numeral:
            val += self.digit_map[char]
        return val
    

class RomanNumeralConverterTest(unittest.TestCase):
    def test_parsing_millenia(self):
        value = RomanNUMERALConverter("M")
        self.assertEqual(1000, value.convert_to_decimal())

    def test_parsing_century(self):
        value = RomanNUMERALConverter("C")
        self.assertEqual(100, value.convert_to_decimal())

    def test_parsing_half_century(self):
        value = RomanNUMERALConverter("L")
        self.assertEqual(50, value.convert_to_decimal())

    def test_parsin_decade(self):
        value = RomanNUMERALConverter("X")
        self.assertEqual(10,value.convert_to_decimal())

    def test_parsing_half_decade(self):
        value= RomanNUMERALConverter("V")
        self.assertEqual(5, value.convert_to_decimal())

    def test_parsin_one(self):
        value = RomanNUMERALConverter("I")
        self.assertEqual(1, value.convert_to_decimal())

    def test_no_roman_numeral(self):
        value = RomanNUMERALConverter(None)
        self.assertRaises(TypeError, value.convert_to_decimal)
    

if __name__=="__main__":
    unittest.main()
    
