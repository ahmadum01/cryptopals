from Challenge_3 import single_bite_xor_decoder
import requests


def single_bite_xor_decoder_for_lists(lines):
    max_score = 0
    correct_line = None
    for i in list_of_hex_lines:
        temp = single_bite_xor_decoder(i)
        if temp['score'] > max_score:
            correct_line = temp
            max_score = correct_line['score']
    return correct_line


if __name__ == '__main__':
    # Reading
    list_ = list_of_hex_lines = requests.get('https://cryptopals.com/static/challenge-data/4.txt').text.split()
    print(single_bite_xor_decoder_for_lists(list_))
