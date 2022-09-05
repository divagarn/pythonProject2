'''from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce,ciphertext, tag = encrypt(input("enter mess: "))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print("correct")
else:
    print(f'plain text: {plaintext}')

if ciphertext == "password":
    print("ok")
else:
    print("no")'''

 #b'v\xe1\x8cW\xfb;\t\xc4'.............
# b'P\xef\x8d\xd0\xdb~\x95i'

'''from Crypto.Cipher import AES
import hashlib

password = "mypassword".encode()
key= hashlib.sha256(password).digest()
mode = AES.MODE_CBC
#iv = 'This is an IV456'
iv = "This is an IV456".encode('utf-8')

def pad_message(message):
    while len(message)%16 !=0:
        message = message + " "
        return

cipher = AES.new(key, mode, iv)
message = "this is the message"
padded_message = pad_message(message)

print(len(padded_message))'''

from Crypto.Cipher import AES
import base64

key = "b'P\xef\x8d\xd0\xdb~\x95i'"

cipher_text = 'password'
cipher_text = base64.b64decode(cipher_text)


decipher = AES.new(key.encode(), AES.MODE_ECB)

print(decipher.decrypt(cipher_text))
