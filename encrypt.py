from cryptography.fernet import Fernet

#Commented out the old way of creating a key, hardcoded instead
#key = Fernet.generate_key()

#with open('mykey.key', 'wb') as mykey:
#    mykey.write(key)

#with open('mykey.key', 'rb') as mykey:
#        key = mykey.read()

#print(key)

key = 'EUcs56-cMCveCXMgxiMxXI9uzUFmaHuqnmQX99PUm-U='

#Encrypting - binds hardcoded key to 'f'
f = Fernet(key)

with open('test.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_test.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#Decrypt
f = Fernet(key)

with open('enc_test.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_test.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)