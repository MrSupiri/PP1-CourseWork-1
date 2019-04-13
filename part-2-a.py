ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
# Convert the ALPHABET to list
ALPHABET = [i for i in ALPHABET]
output_string = ''
input_string = input('Enter a String : ')

key = int(input('Enter the key: '))

for letter in input_string:
    if letter in input_string:
        # ALPHABET.index(letter) returns the index of that letter in the ALPHABET list
        # then we can add the key to that index to get the letter
        # then we take the mod of that so if the letter is x and 10 it cycle back to the beginning of the list
        output_string += ALPHABET[(ALPHABET.index(letter)+key) % 26]
    else:
        output_string += letter

print(f'Encoded String is {output_string}')
