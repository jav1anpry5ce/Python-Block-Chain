from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# key = open('Server.pem', 'r')

# javanKey = RSA.importKey(key.read())
# javanPublicKey = javanKey.publickey()

# message = (b'Hello World')
# encrypt = PKCS1_OAEP.new(javanPublicKey)
# decrypt = PKCS1_OAEP.new(javanKey)

# enc = encrypt.encrypt(message)
# dec = encrypt.decrypt(enc)

# print(enc)
# print(dec)
key = RSA.generate(2048)
with open('Client.pem', 'wb') as s:
    s.write(key.exportKey())
