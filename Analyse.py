def CryptAnalyse(CrypType: int):

    inputF = open('input.txt', 'r', encoding='utf8')
    outputF = open('output.txt', 'w', encoding='utf8')
    result = ''
    inputF = inputF.read()

    print('\nВыберите язык шифртекста:\n1 - Английский\n2 - Русский')
    if int(input()) == 1:
        Alphabet = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
        Alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        if int(input()) == 2:
            Alphabet = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙЧЖШЮЦЩЭФЪЁ'
            Alphabet2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        else:
            print("Error!")
            exit()



    result = ''   
    cur = {}


    for i in range(len(Alphabet)):
        cur[Alphabet[i]] = inputF.count(Alphabet[i].upper()) + inputF.count(Alphabet[i].lower())

    cur = dict(sorted(cur.items(), key=lambda item: item[1], reverse=True))
    
    if CrypType == 1:
        
        for j in range (len(inputF)):
            if inputF[j].isalpha():
                numb = 0
                for i in cur:
                    if inputF[j] == i:
                        result += Alphabet[numb]
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

        for i in range (len(inputF)):
            if inputF[i].isalpha():
                result += Alphabet2[((Alphabet2.index(inputF[i]) - b) * a)  % len(Alphabet2)]
            else:
                result += inputF[i]
    
    outputF.write(result)
    outputF.close()
   
    return "Криптоанализ данного шифротекста выполнен успешно!\n"


