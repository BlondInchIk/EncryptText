# -*- coding: utf-8 -*-
def introMS() -> int:
    print("Данный код реалезует шифрование и расшифрование текста путем шифра простой замены, аффинного шифра и аффинного рекуррентного шифра\n")

    print("Выберете тип операции:\n1 - Зашифрование\n2 - Расшифрование\n3 - Криптоанализ")
    OperType = int(input())
    if OperType != 1 and OperType != 2 and OperType != 3: 
        print("\nError! ВВЕДЕНЫ НЕВЕРНЫЕ ВХОДНЫЕ ДАННЫЕ!")
        exit()


    if OperType == 3:
        print("\nВыберите для какого шифра выполнить криптоанализ:\n1 - Шифр простой замены\n2 - Аффинный шифр")
        CrypType = int(input())
        if CrypType != 1 and CrypType != 2: 
            print("\nError! ВВЕДЕНЫ НЕВЕРНЫЕ ВХОДНЫЕ ДАННЫЕ!")
            exit()
    else:
        if OperType == 1 or OperType == 2:
            print("\nВыберите шифр:\n1 - Шифр простой замены\n2 - Аффинный шифр\n3 - Аффинный рекуррентный шифр")
            CrypType = int(input())
            if CrypType != 1 and CrypType != 2 and CrypType != 3: 
                print("\nError! ВВЕДЕНЫ НЕВЕРНЫЕ ВХОДНЫЕ ДАННЫЕ!")
                exit()
        else:
            print("\nError! ВВЕДЕНЫ НЕВЕРНЫЕ ВХОДНЫЕ ДАННЫЕ!")
            exit()


    if OperType == 1:

        if CrypType == 1:
            print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с исходным открытым текстом\n-key.txt - текстовый файл с ключом вида:\n\n\
            ~~~~~~~~~~~~\n\
            A B C D E...\n\
            B C A D F...\n\
            ~~~~~~~~~~~~\n\
            Две строчки с элементами через пробел\n")

        if CrypType == 2:
            print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с исходным открытым текстом\n-key.txt - текстовый файл с ключом вида:\n\n\
            ~~~~~\n\
            17 10\n\
            ~~~~~\n\
            Cтрочка с двумя элементами через пробел\n")

        if CrypType == 3:
            print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с исходным открытым текстом\n-key.txt - текстовый файл с ключом вида:\n\n\
            ~~~~~\n\
            17 10\n\
            15 7\n\
            ~~~~~\n\
            Две строчки с двумя элементами через пробел\n")

    else:
        
        if OperType == 2:

            if CrypType == 1:
                print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с шифртекстом\n-key.txt - ключ, текстовый файл с ключом вида:\n\n\
                ~~~~~~~~~~~~\n\
                A B C D E...\n\
                B C A D F...\n\
                ~~~~~~~~~~~~\n\
                Две строчки с элементами через пробел\n")

            if CrypType == 2:
                print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с шифртекстом\n-key.txt - ключ, текстовый файл с ключом вида:\n\n\
                ~~~~~\n\
                17 10\n\
                ~~~~~\n\
                Cтрочка с двумя элементами через пробел\n")

            if CrypType == 3:
                print("\nПроверьте существование 2-ух файлов:\n-input.txt- текстовый файл с шифртекстом\n-key.txt - улюч, текстовый файл с ключом вида:\n\n\
                ~~~~~\n\
                17 10\n\
                15 7\n\
                ~~~~~\n\
                Две строчки с двумя элементами через пробел\n")

        else:

            if OperType == 3:
                print("\nПроверьте существование файлов:\n-input.txt- текстовый файл с шифртекстом для частотного криптоанализа")


    if OperType == 1 or OperType == 2 or OperType == 3:
        print("Эти файлы существуют в текущей директории?\n1 - Да\n2 - Нет")
        otvet = int(input())
        if otvet == 1:
            return OperType, CrypType
        else:
            if otvet == 2:
                print("\nError! СОЗДАЙТЕ ВЫШЕУКАЗАННЫЕ ФАЙЛЫ!")
                exit()