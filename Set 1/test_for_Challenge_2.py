import pytest
from Challenge_2 import xor, my_xor


def test1():
    first_hex = '1c0111001f010100061a024b53535009181c'
    second_hex = '686974207468652062756c6c277320657965'
    assert my_xor(first_hex, second_hex) == '746865206b696420646f6e277420706c6179'


def test2():
    first_hex = '111111111111111111111111'
    second_hex = '0'
    assert my_xor(first_hex, second_hex) == '111111111111111111111111'


def test3():
    first_hex = ''
    second_hex = ''
    assert my_xor(first_hex, second_hex) == ''


def test4():
    first_hex = '0'
    second_hex = '0'
    assert my_xor(first_hex, second_hex) == '0'


def test5():
    first_hex = 'abcdef'
    second_hex = 'abcdef'
    assert my_xor(first_hex, second_hex) == '0'


def test6():
    first_hex = '0123456789abcdefABCDEF'
    second_hex = first_hex[::-1]
    assert my_xor(first_hex, second_hex) == xor(first_hex, second_hex)