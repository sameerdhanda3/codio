def modified_caesar_cipher(text, shift, direction):
    result = ""
    for character in text:
        if character.isalpha():
            shift_amount = shift % 26
            if direction == "decrypt":
                shift_amount = -shift_amount
            char_code = ord(character)
            base = ord('A') if character.isupper() else ord('a')
            result += chr((char_code - base + shift_amount) % 26 + base)
        else:
            result += character
    return result


text = input("Enter your message: ")
shift = int(input("Enter shift amount: "))
direction = input("Encrypt or Decrypt? ").lower()


if direction.startswith('e'):
    direction = "encrypt"
elif direction.startswith('d'):
    direction = "decrypt"
else:
    print("Invalid option, defaulting to encrypt.")
    direction = "encrypt"


print("Result:", modified_caesar_cipher(text, shift, direction))
