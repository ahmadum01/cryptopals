def repeating_key_xor_encoder(text, key):
    switch = 0
    result = ''
    for i in range(len(text)):
        temp = hex(ord(text[i]) ^ ord(key[switch]))[2:]
        result += '0' * (2 - len(temp)) + temp
        switch = (switch + 1) % len(key)
    return result


if __name__ == '__main__':
    input_text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    input_key = 'ICE'
    print(repeating_key_xor_encoder(input_text, input_key))
    # 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f