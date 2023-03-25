import pytest
from roman_numbers import roman_numerals_to_int

def test_roman_numerals_to_int():
    assert roman_numerals_to_int("I") == 1, "Должен вывести 1"
    assert roman_numerals_to_int("II") == 2, "Должен вывести 2"
    assert roman_numerals_to_int("III") == 3, "Должен вывести 3"
    assert roman_numerals_to_int("IV") == 4, "Должен вывести 4"
    assert roman_numerals_to_int("V") == 5, "Должен вывести 5"
    assert roman_numerals_to_int("VI") == 6, "Должен вывести 6"
    assert roman_numerals_to_int("VII") == 7, "Должен вывести 7"
    assert roman_numerals_to_int("VIII") == 8, "Должен вывести 8"
    assert roman_numerals_to_int("IX") == 9, "Должен вывести 9"
    assert roman_numerals_to_int("IIII") == None, "Должен вывести None"
    assert roman_numerals_to_int("VVVVVV") == None, "Должен вывести None"
    assert roman_numerals_to_int("VC") == None, "Должен вывести None"
    assert roman_numerals_to_int("MMXXIV") == 2024, "Должен вывести 2024"
    assert roman_numerals_to_int("IIIVX") == None, "Должен вывести None"
    assert roman_numerals_to_int("MMMCMXCIX") == 3999, "Должен вывести 3999"
    assert roman_numerals_to_int("M*III") == None, "Должен вывести None"
