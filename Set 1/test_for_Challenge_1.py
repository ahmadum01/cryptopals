import pytest
from Challenge_1 import *


def test1():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test2():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f'
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test3():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f'
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test4():
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f'.upper()
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test5():
    hex_str = ''
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test6():
    hex_str = 'aaaaaaaaaaaaaaaaaa'
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)


def test7():
    hex_str = '0000000000000000'
    assert hex_to_base64(hex_str) == hex_to_base64_with_libs(hex_str)