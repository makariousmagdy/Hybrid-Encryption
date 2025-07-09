from Cryptodome.Cipher import AES
import base64
from Cryptodome import Random
from Cryptodome.Util import Counter
from os import path
import os
def dec(key,fullpath):
    counter = Counter.new(128)
    c = AES.new(key,AES.MODE_CTR,counter=counter)
    with open(fullpath, 'r+b') as file:
        ciphertext = file.read(16)
        while ciphertext:
            file.seek(-len(ciphertext),1)
            file.write(c.decrypt(ciphertext))
            ciphertext = file.read(16)


key = base64.b64decode(input("Enter AES key in base64: "))
ipath = input("path you want to decrypt it: ")
for dir,subdir,files in os.walk(ipath):
    for file in files:
        fullpath = os.path.join(dir,file)
        print(fullpath)
        dec(key, fullpath)
