# key generation
key = Fernet.generate_key()

# string the key in a file
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
