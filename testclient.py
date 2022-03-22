from cryptography.fernet import Fernet
import socket, os.path, datetime, sys, pickle

def Main():
    host = '127.0.0.1'
    port = 8881

    s = socket.socket()
    s.connect((host, port))

    #Hardcoded Encryption Key
    key = 'EUcs56-cMCveCXMgxiMxXI9uzUFmaHuqnmQX99PUm-U='

    Filename = input("File name and extension: ")
    s.send(Filename.encode('utf-8'))
    s.shutdown(socket.SHUT_WR)
    data = s.recv(1024).decode('utf-8')
    #print(data)
    #msg = s.recv(1024).decode('utf-8')
    #print(msg)
    with open('received_file', 'wb') as f:
            print ('file opened')
            while True:
                print('receiving data...')
                data = s.recv(1024)
        #decrypt
                print('data=%s', (data))
                if not data:
                    break
        # write data to a file
            f.write(data)

            f.close()

    f = Fernet(key)

    with open("encrypted_" + Filename, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open("decrypted_" + Filename, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print('Successfully get the file')
    s.close()
    print('connection closed')
    s.close()

if __name__ == '__main__':
    Main()