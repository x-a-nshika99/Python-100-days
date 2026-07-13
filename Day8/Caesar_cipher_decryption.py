alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def decrypt(cipher_text, shift_amount):
    original_text = ""

    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_amount) % 26
            original_text += alphabet[new_position]
        else:
            original_text += letter

    print(f"Decrypted text: {original_text}")


text = input("Enter encrypted message: ").lower()
shift = int(input("Enter shift number: "))

decrypt(text, shift)