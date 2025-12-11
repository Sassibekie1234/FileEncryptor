import getpass

'''
This is a file encryption tool using the Vigenère cipher. 
This code is written by Sassibekie1234.
'''

def encrypt(plain_text):
   encrypted_text = ''
   # Repeat the key to match the length of the plaintext.
   key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
   # Iterate through each character in the plaintext.
   for i in range(len(plain_text)):
       # Check if the character is an alphabet letter.
       if plain_text[i].isalpha():
           # Calculate the shift based on the corresponding key letter.
           shift = ord(key_repeated[i].upper()) - ord('A')
           # Encrypt uppercase and lowercase letters separately.
           if plain_text[i].isupper():
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
           else:
               encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
       else:
           # If the character is not an alphabet letter, keep it unchanged.
           encrypted_text += plain_text[i]
   # Return the final encrypted text
   return encrypted_text

# Decryption function for the Vigenère cipher
def decrypt(cipher_text):
    decrypted_text = ''
    # Repeat the key to match the length of the ciphertext
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    # Iterate through each character in the ciphertext
    for i in range(len(cipher_text)):
        # Check if the character is an alphabet letter
        if cipher_text[i].isalpha():
            # Calculate the shift based on the corresponding key letter
            shift = ord(key_repeated[i].upper()) - ord('A')
            # Decrypt uppercase and lowercase letters separately
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            # If the character is not an alphabet letter, keep it unchanged
            decrypted_text += cipher_text[i]
    # Return the final decrypted text
    return decrypted_text


# Opening the file and loading it into memory
filename = input("What file do you wanna encrypt/decrypt? ")
with open(filename, "r") as file:
    content = file.read()

# ask wether they want to encrypt or decrypt
while True:
    action = input("Do you wanna encrpyt of decrypt? ")
    if action == "encrypt":
       print("Yessir!")
       encrypt(content)
       break

    elif action == "decrypt":
        print("Yessir")
        decrypt(content)
        break

    else:
       print("Didn't get that...")
       print("To exit press CTRL + C")
       print("Or try again: ")
       
# ask for the key/password
key = getpass.getpass(prompt = "Enter your key:")