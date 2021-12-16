import base64


# With lib
def hex_to_base64_with_libs(hex_str):
    return base64.b64encode(bytes.fromhex(hex_str)).decode()


# My realization.
def hex_to_base64(hex_str):
    """Функция ковертирующая hex в base64"""
    b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'  # Алфавит base64

    if len(hex_str) % 2:  # Исключение выбрасывается, если был подан некорректный аргумент
        raise ValueError('non-hexadecimal number found in hex_to_base64 arg')
    for i in hex_str:
        if i not in '0123456789ABCDEFabcdef':
            raise ValueError('non-hexadecimal number found in hex_to_base64 arg')

    # Преобразовываем hex строку в бинарную строку
    bin_str = [bin(int(hex_str[i: i + 2], 16)) for i in range(0, len(hex_str), 2)]
    bin_str = ''.join(['0' * (8 - len(i[2:])) + i[2:] for i in bin_str])

    # Преобразовываем бинарную строку в строку base64
    result = ''
    for i in range(0, len(bin_str), 6):
        match len(bin_str[i: i + 6]) % 3:
            case 0: result += b64chars[int(bin_str[i: i + 6], 2)]
            case 1: result += b64chars[int(bin_str[i:] + '00', 2)] + '='
            case 2: result += b64chars[int(bin_str[i:] + '0000', 2)] + '=='
    return result


if __name__ == '__main__':
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print('With lib:', hex_to_base64_with_libs(hex_string))
    print('My realization:', hex_to_base64(hex_string))
