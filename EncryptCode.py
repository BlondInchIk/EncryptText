from GetKey import getKey

def Encrypt(OperType, CrypType) -> str:
    keyF = open('key.txt', 'r')
    inputF = open('input.txt', 'r')
    outputF = open('output.txt', 'w')

    key = getKey(CrypType, keyF)
    CrypText = ''
    inputF = inputF.read()

    curstr = ''
    for i in inputF: 
            if i.isalpha(): curstr += i.upper()
            else: curstr += i
    inputF = curstr

    if OperType == 1:

        if CrypType == 1:
            cur = key[0]
            for i in range(len(inputF)):
                    print('2')
                    if not(inputF[i] in key[0]) or not (inputF[i] in key[1]): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = cur.index(inputF[i].upper())
                        CrypText += key[1][curindx]
                else:
                    CrypText += inputF[i]

    else:

        if CrypType == 1:
            cur = key[1]
            for i in range(len(inputF)):
                if inputF[i].isalpha():
                    if not(inputF[i] in key[0]) or not (inputF[i] in key[1]): 
                        print("\nError: КЛЮЧ НЕ ПОДХОДИТ К ДАННОМУ ТЕКСТУ!")
                        exit()
                    else:
                        curindx = cur.index(inputF[i].upper())
                        CrypText += key[0][curindx]
                else:
                    CrypText += inputF[i]

    outputF.write(CrypText)
    outputF.close()
    return "Успешно! Шифртекст записан в output.txt"