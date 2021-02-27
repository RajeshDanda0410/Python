def encrypt(text1,s1):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s1-65) % 26 + 65)
        else:
            result += chr((ord(char) + s1- 97) % 26 + 97)
    print("encrtpted text is : "+result)
    return result

def decrypt(text2,s2):
    decrypted_text = ""
    for i in range(len(text2)):
        char = text2[i]
        if (char.isupper()):
            decrypted_text += chr((ord(char) - s2-65) % 26 + 65)
        else:
            decrypted_text += chr((ord(char) - s2- 97) % 26 + 97)
    print("decrypted text is :"+decrypted_text)
text = input("enter the text to encrypt here:\n")
s=4
x = encrypt(text,s)
decrypt(x,s)