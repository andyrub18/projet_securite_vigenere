#! /usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\n`!@#$%^&*()-=+"

letter_to_index = dict(zip(alphabet,range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, key):
    encrypted = ''

    #On separe le message en plusieurs parties de meme longueur que la cle
    split_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))] # (start, end, stop)
    
    #convertir le message en index et ajouter la cle
    for split in split_message:
        i = 0
        for letter in split:
            number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted

def decrypt(cipher, key):
    decrypted = ''

    #On separe le cipher en plusieurs parties de meme longueur que la cle
    split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))] # (start, end, stop)

    #convertir le cipher en index et ajouter la cle
    for split in split_cipher:
        i = 0
        for letter in split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    #Ecrire le message decrypte

    return decrypted

def crack_key(cypher_text,len_key):
    key=''
    for i in range(len_key):
        j=0
        dico={} 
        most_repeted_time=0
        most_repeted_letter=''
        index=i+j*len_key
        while (index)<len(cypher_text):
            letter=cypher_text[index]
            dico[letter]= dico.get(letter,0) + 1
            if dico[letter]>most_repeted_time:
                most_repeted_letter=letter
            j+=1
            index=i+j*len_key
        key+=chr( abs(ord(most_repeted_letter)-(ord(' ')) % len(alphabet) ))
    return key

def crack(cypher,max_length):
    for i in range(1,max_length):
        print("for a length of {} the key should be {}".format(i,crack_key(cypher,i)))


# def main():
#     key = 'key'
#     message = ""

#     with open('message.txt', 'r') as file:
#         message = file.read()
    
#     encrypted_message = encrypt(message,key)
#     print(encrypted_message)
#     decrypted_message = decrypt(encrypted_message, key)
#     print(decrypted_message)

# main()