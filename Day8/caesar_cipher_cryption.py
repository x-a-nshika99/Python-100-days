alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
text = input("type your massage :\n").lower()
shift = int(input("type the shift number :\n"))

# todo1 : create a function called encrypt() that takes the original_text and shift_amount and print 

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter

    print(f"Encrypted text: {cipher_text}")


text = input("Enter your message: ").lower()
shift = int(input("Enter shift number: "))

encrypt(text, shift)

 