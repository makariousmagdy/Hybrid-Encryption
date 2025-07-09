from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA
import base64
import os
import os.path
private_key = b'-----BEGIN RSA PRIVATE KEY-----\n....'
imported_private_key = RSA.import_key(private_key)
dec = PKCS1_OAEP.new(imported_private_key)
encrypted_key_path = input("enter encrypted_key path: ")
with open(encrypted_key_path, "rb") as f:
    encrypted_key = f.read()
AES_key = dec.decrypt(encrypted_key)
print(base64.b64encode(AES_key).decode())

