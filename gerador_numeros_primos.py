#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:33:17 2018

@author: luizbezerra
"""

def gerador_primos(x):
    lista_primos = [2]
    for i in range(3,x,1):
        restos = []
        qte_primos = len(lista_primos)
        for j in range(0,qte_primos,1):
            temp_primo = lista_primos[j]
            temp_aloc = i % temp_primo
            restos.append(temp_aloc)
        if 0 not in restos:
            lista_primos.append(i)
    return lista_primos

gerador_primos(10000)

# Encotrar maior numero primo divisor: 
    
def maior_primo(valor):
    start_time = time.time()
    lista_primos = gerador_primos(valor)
    resto = []
    for i in range(0, len(lista_primos),1):
        temp = lista_primos[i]
        resto_temp = valor % temp
        resto.append(resto_temp)
    pos = [j for j,x in enumerate(resto) if x == 0]
    maior_divisor = lista_primos[max(pos)]
    print('Maior divisor é {}'.format(maior_divisor))
    print("--- %s seconds ---" % (time.time() - start_time))
    return maior_divisor

maior_primo(600851475143)

import time
start_time = time.time()
600851475143
print("--- %s seconds ---" % (time.time() - start_time))