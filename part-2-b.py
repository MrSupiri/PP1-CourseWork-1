ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = [i for i in ALPHABET]


def decode(input_string, key):
    key = int(key)
    output_string = ''
    for letter in input_string:
        if letter in input_string:
            # Same thing as the encoding but instated of adding now we subtract
            output_string += ALPHABET[(ALPHABET.index(letter)-key) % 26]
        else:
            output_string += letter

    print(f'Decoded String is {output_string}')


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


while True:
    print("Enter 'e' to Enter into Encoding Mode")
    print("Enter 'd' to Enter into Decoding Mode")
    print("Enter 'q' to exit")
    mode = input('$ ')
    if mode == 'e':
        encode(input('Enter a String : '), input('Enter the key: '))
    elif mode == 'd':
        decode(input('Enter a String : '), input('Enter the key: '))
    elif mode == 'q':
        break
    else:
        print('Invalid Input')
    print()
