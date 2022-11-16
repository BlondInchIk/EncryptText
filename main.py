#python 3.10

# шифр простой замены
# аффинный шифр
# аффинный рекуррентный шифр

import os.path
from intro import introMS
from EncryptCode import Encrypt

def start():
    OperType, CrypType = introMS()
    if OperType + CrypType != 0: CheckF(OperType, CrypType) 
    else: 
        print("\nError")
        exit()
    return None

def CheckF(OperType, CrypType):
    if os.path.isfile('key.txt') and os.path.isfile('input.txt'):
        print()
        print(Encrypt(OperType, CrypType))
    else:
        print("\nСОЗДАЙТЕ ВЫШЕУКАЗАННЫЕ ФАЙЛЫ!")
        exit()
    return None

if __name__ == "__main__":
	start()