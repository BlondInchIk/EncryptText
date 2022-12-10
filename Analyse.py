# -*- coding: utf-8 -*-
def CryptAnalyse(CrypType):

    inputF = open('input.txt', 'r', encoding='utf8')
    outputF = open('output.txt', 'w', encoding='utf8')
    result = ''
    inputF = inputF.read()

    print('\nВыберите язык шифртекста:\n1 - Английский\n2 - Русский')
    if int(input()) == 1:
        Alphabet = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
        Alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        Alphabet = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙЧЖШЮЦЩЭФЪЁ'
        Alphabet2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    cur = {}

    for i in range(len(Alphabet)):
        cur[Alphabet[i]] = inputF.count(Alphabet[i].upper()) + inputF.count(Alphabet[i].lower())

    cur = dict(sorted(cur.items(), key=lambda item: item[1], reverse=True))
    print('\n',cur,'\n\n')
    if CrypType == 1:
        
        for j in range (len(inputF)):
            if inputF[j].isalpha():
                numb = 0
                for i in cur:
                    if inputF[j].upper() == i:
                        if inputF[j].upper() == inputF[j]:
                            result += Alphabet[numb].upper()
                        else:
                            result += Alphabet[numb].lower()
                        break
                    numb += 1
            else:
                result += inputF[j]
                    
    else:
        
        x = Alphabet[0]
        for i in cur:
            y = i
            break
        a = 0
        b = 0
        for a2 in range(len(Alphabet)):
            for b2 in range(len(Alphabet)):
                if (Alphabet2.index(x)*a2 + b2) % len(Alphabet2) == Alphabet2.index(y):
                    a = a2
                    b = b2
                    for i in range(len(Alphabet)):
                        if((a * i) % len(Alphabet) == 1):
                            a = i
                            break
                    result = ''
                    for i in range (30):
                        if inputF[i].isalpha():
                            if inputF[i].upper() == inputF[i]:
                                result += Alphabet2[((Alphabet2.index(inputF[i].upper()) - b) * a)  % len(Alphabet2)].upper()
                            else:
                                result += Alphabet2[((Alphabet2.index(inputF[i].upper()) - b) * a)  % len(Alphabet2)].lower()
                        else:
                            result += inputF[i]
                    print("Результат для a = ", a,', и b = ', b, ' = ', result,'\n')

        result = ''
        a = int(input("Выберите a "))
        b = int(input("Выберите b "))
        print(a, b)
        for i in range (len(inputF)):
            if inputF[i].isalpha():
                if inputF[i].upper() == inputF[i]:
                    result += Alphabet2[((Alphabet2.index(inputF[i].upper()) - b) * a)  % len(Alphabet2)].upper()
                else:
                    result += Alphabet2[((Alphabet2.index(inputF[i].upper()) - b) * a)  % len(Alphabet2)].lower()
            else:
                result += inputF[i]
    outputF.write(result)
    outputF.close()
   
    return "Криптоанализ данного шифротекста выполнен успешно!\n"