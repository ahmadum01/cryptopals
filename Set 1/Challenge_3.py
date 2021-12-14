import string


def single_bite_xor_decoder(hex_line):
    """Input: hex_line
        Output: dictionary with key for decode, decoded string and score of frequency analysis.
    """
    def frequency_analysis(text):
        score = 0
        for letter in text:
            if letter in 'ETAOINSHRDLUetaoinshrdlu ':  # The most frequent letters
                score += 3
            elif letter in string.ascii_letters:
                score += 2
            elif letter in '.!?,-\'0123456789':
                score += 1
        return score

    key = ''  # Key for decode
    text_with_max_score = ''  # Result text line, which has the max frequency analysis score value
    max_score = 0  # Frequency analysis score

    for i in range(255):  # Brute force of ASCII characters
        decoded_text = ''
        decoded_text_score = 0
        for j in range(0, len(hex_line), 2):
            xor_ed_string = hex(int(hex_line[j:j + 2], 16) ^ i)[2:]
            decoded_text += chr(int('0' * (2 - len(xor_ed_string)) + xor_ed_string, 16))
            decoded_text_score = frequency_analysis(decoded_text)
        if decoded_text_score > frequency_analysis(text_with_max_score):
            text_with_max_score = decoded_text
            max_score = decoded_text_score
            key = hex(i)[2:]

    return {"key": key, "text": text_with_max_score, "score": max_score}


if __name__ == '__main__':
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(single_bite_xor_decoder(s))
    # {'key': '58', 'text': "Cooking MC's like a pound of bacon", 'score': 90}
