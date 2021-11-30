import re

first_hex = '1c0111001f010100061a024b53535009181c'
second_hex = '686974207468652062756c6c27732065796'


# with standard functions
def xor(first, second):
    # check for empty string
    if len(first) == 0 and len(second) == 0:
        return ''
    if len(first) == 0:
        first = '0'
    if len(second) == 0:
        second = '0'
    return hex(int(first, 16) ^ int(second, 16))[2:]


# manual xor realisation
def my_xor(first, second):
    """Inputs: 'first' and 'second' are hex-strings
        Output: xor of first and second hex-strings
     """
    # check for invalid symbol with using regEx
    if re.match(r'[\dabcdefABCDEF]*', first).group(0) != first:
        raise 'invalid symbol in first argument'
    if re.match(r'[\dabcdefABCDEF]*', second).group(0) != second:
        raise 'invalid symbol in second argument'

    # check for empty string
    if len(first) == 0 and len(second) == 0:
        return ''
    if len(first) == 0:
        first = '0'
    if len(second) == 0:
        second = '0'

    # Translate from hex to bin
    first_bin = bin(int(first, 16))[2:]
    second_bin = bin(int(second, 16))[2:]

    # Adding leading zeros
    first_bin = '0' * (max(len(second), len(first)) * 4 - len(first_bin)) + first_bin
    second_bin = '0' * (max(len(second), len(first)) * 4 - len(second_bin)) + second_bin

    # xor
    result = ''
    for i, j in zip(first_bin, second_bin):
        result += '0' if i == j else '1'
    return hex(int(result, 2))[2:]


# print('XOR with standard functions:', xor(first_hex, second_hex))
# print('manual xor realisation:     ', my_xor(first_hex, second_hex))