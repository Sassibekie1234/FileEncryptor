import getpass

'''
This is a file encryption tool using the Vigenère cipher. 
This code is written by Sassibekie1234.
'''

def encrypt(text):
    print("Still working on this")

def decrypt(text):
    print("Still working on this")

print("Hello, World!")
print("This is beeing worked on")

# Opening the file and loading it into memory
filename = input("What file do you wanna encrypt? ")
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