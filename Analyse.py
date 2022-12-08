def CryptAnalyse(CrypType: int):

    inputF = open('input.txt', 'r', encoding='utf8')
    result = ''
    inputF = inputF.read()

    # print('\nВыберите язык шифртекста:\n1 - Английский\n2 - Русский')
    # if int(input()) == 1:
    #     Alphabet = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
    # else:
    #     if int(input()) == 2:
    #         Alphabet = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙЧЖШЮЦЩЭФЪЁ'
    #     else:
    #         print("Error!")
    #         exit()
    
    Alphabet = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙЧЖШЮЦЩЭФЪЁ'
    cur = {}

    if CrypType == 1:
        for i in range(len(Alphabet)):
            cur[Alphabet[i]] = inputF.count(Alphabet[i].upper()) + inputF.count(Alphabet[i].lower())

    cur = dict(sorted(cur.items(), key=lambda item: item[1], reverse=True))
    return cur

print(CryptAnalyse(1))