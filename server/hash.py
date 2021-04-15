import json
# from .models import User
# # ! Hash
# import bcrypt
# pwd = bytes(input("Password ??"), 'utf-8')

# hash = bcrypt.hashpw(pwd, bcrypt.gensalt())

# hash = b'$2b$12$889xpznjPrcEnoIRl11LCeVyidvkUUs7DXnfmSWhw9dbf68nkGPTm'
# # print(hash)
# if bcrypt.checkpw(pwd, hash):
#     print("True")
# else:
#     print("false")


# def check_user(password, hashed_pswd):
#     if bcrypt.checkpw(password, hashed_pswd):
#         return True
#     else:
#         return False

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

# myModel = User()
# listIWantToStore = [1, 2, 3, 4, 5, 'hello']
# json_list = json.dumps(listIWantToStore)
# print(type(json_list))
# jsonDec = json.decoder.JSONDecoder()
# real_list = jsonDec.decode("")
# print(type(real_list))
# real_list.append('new_item')
# print(real_list)
# json_list = json.dumps(listIWantToStore)
# print(type(json_list))
# print(json_list)

# myModel.save()
