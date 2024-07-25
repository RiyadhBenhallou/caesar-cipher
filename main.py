from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    result = ''
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            result += alphabet[alphabet.index(letter) + shift]
        else:
            result += letter

    print(f'The {direction}d text is: {result}')

answer = 'yes'

print(logo)
while answer == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= int(len(alphabet) / 2)
    caesar(direction, text, shift)
    answer = input('do you want to continue?\n').lower()


print('Goodbye!')