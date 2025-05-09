from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes
import time

plaintext = b"This is my message"
des_key = b"8bytekey"
aes_key = b"thisisa16bytekey" 

des_iv = get_random_bytes(8)

des_start = time.time()
des = DES.new(des_key, DES.MODE_OFB, iv=des_iv)
des_end = time.time()
print("DES encryption time: ", des_end - des_start)

aes_start = time.time()
aes = AES.new(aes_key, AES.MODE_EAX)
aes_end = time.time()
print("AES encryption time: ", aes_end - aes_start)

aes_nonce = aes.nonce

des_ciphertext = des.encrypt(plaintext)
aes_ciphertext = aes.encrypt(plaintext)

print(f"The DES-encrypted ciphertext is: {des_ciphertext}")
print(f"The AES-encrypted ciphertext is: {aes_ciphertext}")

print(f"Length of DES ciphertext: {len(des_ciphertext)}")
print(f"Length of AES ciphertext: {len(aes_ciphertext)}")

des = DES.new(des_key, DES.MODE_OFB, iv=des_iv)
aes = AES.new(aes_key, AES.MODE_EAX, nonce=aes_nonce)

des_plaintext = des.decrypt(des_ciphertext)
aes_plaintext = aes.decrypt(aes_ciphertext)

print(f"The DES-decrypted text is: {str(des_plaintext)}")
print(f"The AES-decrypted text is: {str(aes_plaintext)}")