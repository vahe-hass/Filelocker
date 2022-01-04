from cryptography.fernet import Fernet
from pathfinder import *

class Cipher:

    # This Keys should be created in windows env so they can not be seen.
    key1 = b'rQshcKens5ICQFXUdVeCCZguSBsuxioL158Kx8vDuWI='
    key2 = b'cfpPAZTzuJoVRFhveau0rc-MTVGD7x03FvmzaZYqtB0='


    def __init__(self):
        pass


    def encryptfile(file):
        with open(file, 'rb') as f:
            data = f.read()

        fernet = Fernet(Cipher.key1)
        encrypted = fernet.encrypt(data)

        with open(file, 'wb') as f:
            f.write(encrypted)

    def decryptfile(file):
        with open(file, 'rb') as f:
            data = f.read()

        fernet = Fernet(Cipher.key1)
        decrypted = fernet.decrypt(data)

        with open(file, 'wb') as f:
            f.write(decrypted)

    def encryptfiles(file_list, location):
        directory_change = location
        for i in file_list:
            with open(i, 'rb') as f:
                data = f.read()

            fernet = Fernet(Cipher.key2)
            encrypted = fernet.encrypt(data)

            with open(i, 'wb') as f:
                f.write(encrypted)


    def decryptfiles(file_list, location):
        directory_change = location
        for i in file_list:
            with open(i, 'rb') as f:
                data = f.read()

            fernet = Fernet(Cipher.key2)
            encrypted = fernet.decrypt(data)

            with open(i, 'wb') as f:
                f.write(encrypted)

if __name__ == "__main__":
    Cipher()
