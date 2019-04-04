from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    encryptedText = ""
    
    for aLetter in text:
        encryptedText += rotate_character (aLetter, rot)
        
    return encryptedText 

def main():
    userText = input("Enter text to encrypt")
    userRot = input("What is your encrytion key?")
    userRot = int(userRot)

    print(encrypt(userText, userRot))



if __name__ == "__main__":
    main()