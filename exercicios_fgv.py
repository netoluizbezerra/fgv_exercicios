#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:05:10 2018

@author: luizbezerra
"""

#Fução implementa collatz
def collatz(x):
    seq = [x]
    if x == 1: 
        return []
    while x != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1
        seq.append(x)
    return seq
        
      
def palindromo_prod(x):
    list1 = list(range(100,x,1))
    list2 = list(range(100,x,1))
    produto = []
    for j in range(1, len(list1)):
        for i in range(1,len(list1)):
            prod_temp = list1[i] * list2[j]
            produto.append(prod_temp)
    return produto

def palindromo(x):
    produto = palindromo_prod(x)
    palindromo = []
    for j in range(1,len(produto)):
        string_produto = str(produto[j])
    if string_produto == string_produto[-1::-1]:
        palindromo.append(int(string_numero)) 
    return palindromo

for j in range(1,len(produto)):
    print(j)
        
        
list1 = list(range(100,1000,1))
    


def operacao(x,y,z):
    if z == "divisao":
        n = x/y
    elif z == "soma":
        n = x + y
    elif z == "subtacao":
        n = x - y
    elif z == "multiplicacao":
        n = x * y
    else: 
        print('entrar com nome valido')
        return n

 
def fatorial(x):
    import math
    lista_fatoriais_curiosos = [1]
    for i in range(1,x,1):
        temp_numero = 10 + i
        if temp_numero < 100:
            str_numero = str(temp_numero)
            dezena = str_numero[0]
            unidade = str_numero[1]
            temp_soma_fatorial = math.factorial(int(dezena)) + math.factorial(int(unidade))
            if temp_numero == temp_soma_fatorial: 
                 lista_fatoriais_curiosos.append(temp_numero)    
        elif temp_numero >= 100 and temp_numero < 1000:
            str_numero = str(temp_numero)
            centena = str_numero[0]
            dezena = str_numero[1]
            unidade = str_numero[2]
            temp_soma_fatorial = math.factorial(int(dezena)) + math.factorial(int(unidade)) + math.factorial(int(centena))
            if temp_numero == temp_soma_fatorial: 
                 lista_fatoriais_curiosos.append(temp_numero)
        elif temp_numero >= 1000 and temp_numero < 10000:
            str_numero = str(temp_numero)
            milhar = str_numero[0]
            centena = str_numero[1]
            dezena = str_numero[2]
            unidade = str_numero[3]
            temp_soma_fatorial = math.factorial(int(milhar)) + math.factorial(int(dezena)) + math.factorial(int(unidade)) + math.factorial(int(centena))
            if temp_numero == temp_soma_fatorial: 
                 lista_fatoriais_curiosos.append(temp_numero)
        elif temp_numero >= 10000 and temp_numero < 100000:
            str_numero = str(temp_numero)
            dezena_milhar = str_numero[0]
            milhar = str_numero[1]
            centena = str_numero[2]
            dezena = str_numero[3]
            unidade = str_numero[4]
            temp_soma_fatorial = math.factorial(int(dezena_milhar)) + math.factorial(int(milhar)) + math.factorial(int(dezena)) + math.factorial(int(unidade)) + math.factorial(int(centena))
            if temp_numero == temp_soma_fatorial: 
                 lista_fatoriais_curiosos.append(temp_numero)
    return lista_fatoriais_curiosos

    
    
    
    
    
    
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    