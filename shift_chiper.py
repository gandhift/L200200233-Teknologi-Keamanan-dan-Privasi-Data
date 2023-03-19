def encrypt_shift_cipher(input_text, key):
    output_text = ''
    for char in input_text:
        if char.isdigit():
            shifted_digit = (int(char) + key) % 10
            output_text += str(shifted_digit)
        else:
            output_text += char
    return output_text


def decrypt_shift_cipher(ciphered_text, key):
    output_text = ''
    for char in ciphered_text:
        if char.isdigit():
            shifted_digit = (int(char) - key) % 10
            output_text += str(shifted_digit)
        else:
            output_text += char
    return output_text


input_text = '33'
key = 3
ciphered_text = encrypt_shift_cipher(input_text, key)
print("pesan yang dienkripsi ", ciphered_text)
decrypted_text = decrypt_shift_cipher(ciphered_text, key)
print("pesan yang didekripsi ", decrypted_text)
