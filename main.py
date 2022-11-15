#python 3.10

# шифр простой замены
# аффинный шифр
# аффинный рекуррентный шифр

from intro import introMS

def start():
    OperType, CrypType = introMS()
    if OperType + CrypType != 0: CheckF(OperType, CrypType)
    return None

def CheckF(OperType, CrypType):
    print(OperType, CrypType)
    input('Нажмите Enter для выхода\n')
    return None

if __name__ == "__main__":
	start()