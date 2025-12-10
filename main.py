import getpass

'''
This is a file encryption tool using the Vigenère cipher. 
This code is written by Sassibekie1234.
'''

def encrypt(text):
    lines = len(text)
    print("Still working on this")

def decrypt(text):
    print("Still working on this")

print("Hello, World!")
print("This is beeing worked on")

filename = input("What file do you wanna encrypt?")
with open("geek.txt", "r") as file:
    content = file.read()
    print(content)


# ask wether they want to encrypt or decrypt
action = input("Do you wanna encrpyt of decrypt? ")
# ask for the key/password
key = getpass.getpass(prompt = "Enter your key:")
# make a new file containing the encrypted/decrypted text


