ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = [i for i in ALPHABET]


def analyze(input_string, output_string):
    # print(input_string, output_string)
    keys = []
    # iterate though the letters of the both string up max index of the string with the lowest characters
    # going thought the every letter to find if there is any other pattern we extract and let the user decide what to do
    for i in range(min(len(input_string), len(output_string))):
        try:
            letter_index_1 = ALPHABET.index(input_string[i])
            letter_index_2 = ALPHABET.index(output_string[i])
            key = letter_index_1-letter_index_2
            if key < 0:
                key = 26 + key
            if key not in keys:
                keys.append(key)
        # Very Character from the input or output string might not be from the ALPHABET
        except ValueError:
            continue

    if len(keys) == 0:
        print('[ERROR] Encoded String or the part of Decoded String didn\'t contain any letters from the Alphabet')
    elif len(keys) == 1:
        decode(input_string, keys[0])
    else:
        print('[INFO] There are more than one possible output strings')
        for key in keys:
            print('>', decode(input_string, key, print_2_SOUT=False))


def decode(input_string, key, print_2_SOUT=True):
    # Verifying the key is integer
    try:
        key = int(key)
    except ValueError:
        print('Key Must be a Integer, Try Again !')
        return False

    output_string = ''
    for letter in input_string:
        if letter in input_string:
            # Same thing as the encoding but instated of adding now we subtract
            output_string += ALPHABET[(ALPHABET.index(letter)-key) % 26]
        else:
            output_string += letter
    if print_2_SOUT:
        print(f'Decoded String is {output_string}')
    else:
        return output_string


def encode(input_string, key):
    # Verifying the key is integer
    try:
        key = int(key)
    except ValueError:
        print('Key Must be a Integer, Try Again !')
        return False

    output_string = ''
    for letter in input_string:
        if letter in input_string:
            # ALPHABET.index(letter) returns the index of that letter in the ALPHABET list
            # then we can add the key to that index to get the letter
            # then we take the mod of that so if the letter is x and 10 it cycle back to the beginning of the list
            output_string += ALPHABET[(ALPHABET.index(letter)+key) % 26]
        else:
            output_string += letter

    print(f'Encoded String is {output_string}')


print("Enter 'a' to Enter into Analyzing Mode")
print("Enter 'e' to Enter into Encoding Mode")
print("Enter 'd' to Enter into Decoding Mode")
print("Enter 'q' to exit")

while True:
    mode = input('$ ').strip()
    if mode == 'e':
        encode(input('Enter a String : '), input('Enter the key: '))
    elif mode == 'd':
        decode(input('Enter a String : '), input('Enter the key: '))
    elif mode == 'a':
        analyze(input('Enter a String Encoded String : '),
                input('Enter a part of Decoded String: '))
    elif mode == 'q':
        break
    elif mode == '':
        continue
    else:
        print('Invalid Input')
    print()
