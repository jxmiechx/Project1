from cryptography.fernet import Fernet
import socket
import os

def Main():
    host = '127.0.0.1'
    port = 8881

    s = socket.socket()
    s.bind((host,port))
    print("Server", host, "waiting on port", port)
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Connected to: " + str(addr))
        filename = ''
        while True:
            data = c.recv(1024).decode('utf-8')
            if not data:
                break
            filename += data
        print("---------------------------") #making it easier to read on terminal
        print("File requested: " + filename)
        if os.path.isfile(filename):
            file2send = open(filename, "rb")

            key = 'EUcs56-cMCveCXMgxiMxXI9uzUFmaHuqnmQX99PUm-U='

#Encrypting - binds hardcoded key to 'f'
            f = Fernet(key)

            with open(filename, 'rb') as original_file:
                original = original_file.read()

            encrypted = f.encrypt(original)

            with open("encrypted_" + filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            c.send(file2send.read())
            c.close()
            print("--ENCRYPTED FILE SENT TO CLIENT--")
            break

        else:
            print("File not found")
            msg = ('File not found')
            break
            #s.send(msg.encode('utf-8'))
            

if __name__ == '__main__':
    Main()
    
