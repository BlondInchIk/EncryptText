def CryptAnalyse(CrypType: int):

    inputF = open('input.txt', 'r', encoding='utf8')
    result = ''
    inputF = inputF.read()

    print('\nВыберите язык шифртекста:\n1 - Английский\n2 - Русский')
    if int(input()) == 1:
        Alphabet = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
    else:
        if int(input()) == 2:
            Alphabet = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙЧЖШЮЦЩЭФЪЁ'
        else:
            print("Error!")
            exit()
    
    
    cur = {}


    for i in range(len(Alphabet)):
        cur[Alphabet[i]] = inputF.count(Alphabet[i].upper()) + inputF.count(Alphabet[i].lower())

    cur = dict(sorted(cur.items(), key=lambda item: item[1], reverse=True))
    
    if CrypType == 1:
        numb = 0
        for i in cur:
            inputF = inputF.replace(i, Alphabet[numb])
            numb += 1
    else:
        x = Alphabet[0]
        for i in cur:
            y = i
        a = 0
        b = 0
        for a2 in range(len(Alphabet)):
            for b2 in range(len(Alphabet)):
                if (Alphabet2.index(x)*a2 + b2) % len(Alphabet) == Alphabet2.index(y):
                    a = a2
                    b = b2

        for i in inputF:
            
    print("Криптоанализ данного шифротекста выполнен успешно!\n")
    return inputF

print("Криптоанализ данного шифротекста:\n",CryptAnalyse(1))
