################### The first way. ###################
import codecs
s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()
print('First way:',b64)


################### The second way. ###################
from base64 import b64encode, b64decode
s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = b64encode(bytes.fromhex(s)).decode()
print('Second way:', b64, end='\n\n')


################### The third way. My realization. ###################
def hex_to_base64(hex_str):
	'''Функция ковертирующая hex в base64'''

	b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/' # Алфавит base64

	if len(hex_str) % 2:#Исключение: выбрасывается, если аргумент некорректный'''	
		raise ValueError('non-hexadecimal number found in hex_to_base64 arg')
	for i in hex_str:
		if i not in '0123456789ABCDEFabcdef':
			raise ValueError('non-hexadecimal number found in hex_to_base64 arg')

	padding_with_zeros = lambda num: '0' * (8 - len(num)) + num # Функция дополняющая число нулями слева(до 8 символов)

	bin_str = map(bin, (map(lambda num: int(num, 16), [hex_str[i * 2: i * 2 + 2] for i in range(len(hex_str)//2)])))
	formated_bin_str = ''.join([padding_with_zeros(i[2:]) for i in bin_str])
	result = ''
	for i in range(len(formated_bin_str)//6):
		result += b64chars[int(formated_bin_str[i * 6 : i * 6 + 6], 2)]

	match len(formated_bin_str) % 3:
		case 1: result += '='
		case 2: result += '=='
		case _: None
	return result


s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = hex_to_base64(s)
print('Third way:', b64)