# -*- coding: utf-8 -*-
def getKey(CrypType, keyF):

    if CrypType == 1:
        s1 = keyF.readline()
        key = 0
        s1_ = ''
        for i in s1: 
            if i.isalpha(): s1_ += i.upper() + ' ' 
            else: s1_ += i + ' '
            key += 1
        s1_ = s1_.split()

        s2 = keyF.readline()
        key = 0
        s2_ = ''
        for i in s2: 
            if i.isalpha(): s2_ += i.upper() + ' ' 
            else: s2_ += i + ' '
            key += 1
        s2_ = s2_.split()
    
    if CrypType == 2:
        s1 = keyF.readline()
        key = 0
        s1_ = ''
        for i in s1: 
            if i.isalpha(): s1_ += i.upper()
            else: s1_ += i
            key += 1
        s1_ = s1_.split()

    if CrypType == 3:
        s1 = keyF.readline()
        key = 0
        s1_ = ''
        for i in s1: 
            if i.isalpha(): s1_ += i.upper() 
            else: s1_ += i
            key += 1
        s1_ = s1_.split()

        s2 = keyF.readline()
        key = 0
        s2_ = ''
        for i in s2: 
            if i.isalpha(): s2_ += i.upper() 
            else: s2_ += i
            key += 1
        s2_ = s2_.split()

    cur = [] * len(s1_)
    otvet = [cur] * 2
    otvet[0]= s1_
    if CrypType == 1 or CrypType == 3:
        otvet[1] = s2_

    return otvet
