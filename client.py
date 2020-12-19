#! /usr/bin/env python3


import socket
from vigenere import decrypt

s = socket.socket()
host = input(str("Entrez l'address de l'envoyeur s'il vous plait: "))
port = 8080
s.connect((host,port))
print("Connected ... ")

file = open('message1.txt', 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()

with open ('message1.txt','r') as file:
    message = file.read()

decrypted_message = decrypt(message,'key')

with open ('message_recu.txt','w') as file:
    file.write(decrypted_message)


print("Le fichier a ete recu avec succes")