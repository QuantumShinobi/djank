
# ! Hash
import bcrypt
pwd = bytes(input("Password ??"), 'utf-8')

hash = bcrypt.hashpw(pwd, bcrypt.gensalt())

hash = b'$2b$12$889xpznjPrcEnoIRl11LCeVyidvkUUs7DXnfmSWhw9dbf68nkGPTm'
# print(hash)
if bcrypt.checkpw(pwd, hash):
    print("True")
else:
    print("false")


def check_user(password, hashed_pswd):
    if bcrypt.checkpw(password, hashed_pswd):
        return True
    else:
        return False

# # ! Encrypt-Decrypt
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# string = "Hi, Im Rishit".encode()
# a = Fernet(key)
# coded_string = a.encrypt(string)
# print(coded_string)

# decoded_string = str(a.decrypt(coded_string))
# print(decoded_string)
# print(type(decoded_string))
