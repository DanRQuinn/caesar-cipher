from caesar_cipher.corpus_loader import word_list, name_list

def encrypt(text, shift):
    """Encrypts a string using the Caesar Cipher method.

    Args:
        text (str): The text to be encrypted.
        shift (int): The number of characters to shift the text.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypts a string using the Caesar Cipher method.

    Args:
        text (str): The text to be decrypted.
        shift (int): The number of characters to shift the text.

    Returns:
        str: The decrypted text.
    """
    return encrypt(text, -shift)

def crack(encrypted_text):
    for shift in range(26):
        counter = 0
        unencrypted_text = encrypt(encrypted_text, shift)
        list_word = unencrypted_text.split()
        for letter in list_word:
            if letter in name_list or letter in word_list:
                counter += 1
        if (counter/len(list_word)) > .5:
          return ' '.join(list_word)
    return ''
