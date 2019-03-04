#Sk Ayon
#Simple Caesar Cipher

def encrypt(text, even_key, odd_key, direction = 1):
    index = 0
    even_key *= direction
    odd_key *= direction
    encrypted = ""
    for i in text:
        i = ord(i)
        if index % 2 == 0:
            i += even_key
        else:
            i += odd_key
        if(i > 126):                   #since we add, it might go over 126 in which case we have to add to roll back
            i = i % 94 + 32
        encrypted += chr(i)
    print("Original text: " + text + "\n" + "Encrypted text: " + encrypted)

def decrypt(encText, even_key, odd_key, direction = 1):
    index = 0
    even_key *= direction
    odd_key *= direction
    decrypted = ""
    for i in encText:
        i = ord(i)
        if index % 2 == 0:
            i -= even_key
        else:
            i -= odd_key
        if(i < 32):
            i += 94
        print(str(i) + " this is char after conversion")
        decrypted += chr(i)
    print("Original encryption: " + encText + "\n" + "Decrypted text: " + decrypted)

def getMessage():
    text = input("Type the message you would like to encrypt/decrypt: ")
    for i in text:
        i = ord(i)
    return text

def getKeys():
    keys = input("Type the even key followed by whitespace and then type the odd key. Note: the keys have to both be between 1 and 94 inclusive ")
    keyList = keys.split()
    return keyList
        
def main():
    message = getMessage()
    keys = getKeys()
    e_key = int(keys[0])
    o_key = int(keys[1])
    enc_or_dec = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt ")
    enc_or_dec = str.lower(enc_or_dec)
    if enc_or_dec == "encrypt":
        print(message)
        encrypt(message,e_key,o_key)
    elif enc_or_dec == "decrypt":
        decrypt(message,e_key,o_key)
    else:
        print("Invalid command")

main()
    
