import string

def decryptText(cipherText, key):
    plainText = "";
    for i in cipherText:
        temp = ord(i);
        if ((temp >= ord('A')) and (temp <= ord('Z'))):
            if (temp - ord('A') < key):
                plainText += chr((temp - ord('A') + 26 - key) + ord('A'));
            else:
                plainText += chr((temp - ord('A') - key) + ord('A'));
        else:
            if ((temp >= ord('a')) and (temp <= ord('z'))):
                if (temp - ord('a') < key):
                    plainText += chr((temp - ord('a') + 26 - key) + ord('a'));
                else:
                    plainText += chr((temp - ord('a') - key) + ord('a'));
            else:
                plainText += i;
    return plainText;

def checkIfKeyWorks(plainText):
    with open("Words.txt", "r") as reader:
        words = reader.readlines();
    for word in words:
        if (plainText.find(str(word)) != -1):
            return True;
    return False;

def CaesarDecrypter(cipherText):
    """ FIND A KEY AND DECRYPT THE CIPHERTEXT """
    for i in range(1, 26):
        plainText = decryptText(cipherText, i);
        if (checkIfKeyWorks(plainText)):
            return i, plainText;
    return -1, "";

def CaesarEncrypter(plainText, key):
    cipherText = "";
    for i in plainText:
        temp = ord(i);
        if ((temp >= ord('A')) and (temp <= ord('Z'))):
            cipherText += chr((temp - ord('A') + key) % 26 + ord('A'));
        else:
            if ((temp >= ord('a')) and (temp <= ord('z'))):
                cipherText += chr((temp - ord('a') + key) % 26 + ord('a'));
            else:
                cipherText += i;
    return cipherText;

if __name__ == "__main__":
    """ READ CIPHERTEXT """
    with open("Encrypted_Text.txt", "r") as reader:
        cipherText = str(reader.read());
    print("The provided cipher text is: ");
    print(cipherText); print();

    """ DECRYPT THE TEXT """
    key, plainText = CaesarDecrypter(cipherText);
    print("The key was used is:", key, "( A ->", chr(key + ord('A')), ")");
    print("The plain text is: ");
    print(plainText); print();

    """ ENCRYPT THE TEXT """
    print("The ciphertext with key = 4 is:");
    print(CaesarEncrypter(plainText, 4));
