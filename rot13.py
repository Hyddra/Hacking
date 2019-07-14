#!/usr/bin/python3

import codecs

# Simple script to solve one of the ROT-13 challenges

enc = codecs.getencoder("rot-13")
dec = codecs.getdecoder("rot-13")

def menu():
    print("Pick one: ")
    print("[1] -> Encryption ")
    print("[2] -> Decryption ")
    print("[q] -> Quit ")
    

menu()

choose = int(input("Pick one: "))

if choose == 1:
    # Now we Encrypt with the shitty cipher
    crypt = input("Pass the string to encode: ")
    encoder = enc(crypt)[0]
    print(encoder)
elif choose == 2:
    # Now we Decrypt the shitty cipher
    crypt = input("Pass the string to decode: ")
    decoder = dec(crypt)[0]
    print(decoder)

