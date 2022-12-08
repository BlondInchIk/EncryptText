# -*- coding: utf-8 -*-
import math
from GetKey import getKey

def Encrypt(OperType, CrypType) -> str:
    keyF = open('key.txt', 'r', encoding='utf8')
    inputF = open('input.txt', 'r', encoding='utf8')
    outputF = open('output.txt', 'w', encoding='utf8')

    key = getKey(CrypType, keyF)
    CrypText = ''
    inputF = inputF.read()
    # curstr = ''
    # for i in inputF: 
    #         if i.isalpha(): curstr += i.upper()
    #         else: curstr += i
    # inputF = curstr

    if CrypType != 1:
        print('\nВыберите язык текста:\n1 - Английский\n2 - Русский')
        if int(input()) == 1:
            Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        else:
            Alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    if OperType == 1:

        if CrypType == 1:
            cur = key[0]
            for i in cur:
                i = i.upper()
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not((inputF[i].upper() in key[0]) or (inputF[i].lower() in key[0])) or not ((inputF[i].upper() in key[1]) or (inputF[i].lower() in key[1])): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = cur.index(inputF[i].upper())
                        if inputF[i].upper() == inputF[i]:
                            CrypText += key[1][curindx].upper()
                        else:
                            CrypText += key[1][curindx].lower()
                else:
                    CrypText += inputF[i]
        
        if CrypType == 2:
            a = int(key[0][0])
            b = int(key[0][1])
            if (math.gcd(a, len(Alphabet))) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not(inputF[i].upper() in Alphabet): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = Alphabet.index(inputF[i].upper())
                        cur = (a*curindx + b) % len(Alphabet)
                        if inputF[i].upper() == inputF[i]:
                            CrypText += Alphabet[cur].upper()
                        else:
                            CrypText += Alphabet[cur].lower()
                else:
                    CrypText += inputF[i]

        if CrypType == 3:
            a = int(key[0][0])
            a1 = int(key[1][0])
            b = int(key[0][1])
            b1 = int(key[1][1])
            numb = 0
            if math.gcd(a, len(Alphabet)) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            if math.gcd(a1, len(Alphabet)) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not(inputF[i].upper() in Alphabet): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = Alphabet.index(inputF[i].upper())
                        if numb == 0:
                            cur = (a*curindx + b) % len(Alphabet)
                            numb += 1
                        else:
                            if numb == 1:
                                cur = (a1*curindx + b1) % len(Alphabet)
                                numb += 1
                            else:
                                cur_a1 = a1
                                cur_b1 = b1
                                a1 = (a * a1) % len(Alphabet)
                                b1 = (b + b1) % len(Alphabet)
                                a = cur_a1
                                b = cur_b1
                                cur = (a1*curindx + b1) % len(Alphabet)
                        if inputF[i].upper() == inputF[i]:
                            CrypText += Alphabet[cur].upper()
                        else:
                            CrypText += Alphabet[cur].lower()
                else:
                    CrypText += inputF[i]


    else:

        if CrypType == 1:
            cur = key[1]
            for i in cur:
                i = i.upper()
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not((inputF[i].upper() in key[0]) or (inputF[i].lower() in key[0])) or not ((inputF[i].upper() in key[1]) or (inputF[i].lower() in key[1])): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = cur.index(inputF[i].upper())
                        if inputF[i].upper() == inputF[i]:
                            CrypText += key[0][curindx].upper()
                        else:
                            CrypText += key[0][curindx].lower()
                else:
                    CrypText += inputF[i]

        if CrypType == 2:
            a = int(key[0][0])
            b = int(key[0][1])
            if math.gcd(a, len(Alphabet)) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            for i in range(len(Alphabet)):
                if((a * i) % len(Alphabet) == 1):
                    a = i
                    break
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not(inputF[i].upper() in Alphabet): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = Alphabet.index(inputF[i].upper())
                        cur = ((curindx - b) * a)  % len(Alphabet)
                        if inputF[i].upper() == inputF[i]:
                            CrypText += Alphabet[cur].upper()
                        else:
                            CrypText += Alphabet[cur].lower()
                else:
                    CrypText += inputF[i]
        
        if CrypType == 3:
            a = int(key[0][0])
            a1 = int(key[1][0])
            b = int(key[0][1])
            b1 = int(key[1][1])
            numb = 0
            if math.gcd(a, len(Alphabet)) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            if math.gcd(a1, len(Alphabet)) != 1:
                print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                exit()
            for i in range(len(Alphabet)):
                if((a * i) % len(Alphabet) == 1):
                    a = i
                    break
            for i in range(len(Alphabet)):
                if((a1 * i) % len(Alphabet) == 1):
                    a1 = i
                    break
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not(inputF[i].upper() in Alphabet): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = Alphabet.index(inputF[i].upper())
                        if numb == 0:
                            cur = ((curindx - b) * a)  % len(Alphabet)
                            numb += 1
                        else:
                            if numb == 1:
                                cur = ((curindx - b1) * a1)  % len(Alphabet)
                                numb += 1
                            else:
                                cur_a1 = a1
                                cur_b1 = b1
                                a1 = (a * a1) % len(Alphabet)
                                b1 = (b + b1) % len(Alphabet)
                                a = cur_a1
                                b = cur_b1
                                cur = ((curindx - b1) * a1)  % len(Alphabet)
                        if inputF[i].upper() == inputF[i]:
                            CrypText += Alphabet[cur].upper()
                        else:
                            CrypText += Alphabet[cur].lower()
                else:
                    CrypText += inputF[i]

    outputF.write(CrypText)
    outputF.close()
    return "Успешно! Шифртекст записан в output.txt"