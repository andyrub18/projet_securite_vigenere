#! /usr/bin/env python3

import socket
from vigenere import encrypt

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("En attente de connection ... ")
conn, addr = s.accept()
print(addr, "est connecte au serveur")

with open('message.txt','r') as file:
    message = file.read()

encrypted_message = encrypt(message, 'key')

with open ('message_encrypte.txt','w') as file:
    file.write(encrypted_message)

file = open('message_encrypte.txt','rb')
file_data = file.read(1024)
conn.send(file_data)
print("Le fichier a ete envoye avec success!")