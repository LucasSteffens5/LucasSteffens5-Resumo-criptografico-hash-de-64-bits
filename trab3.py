#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:38:29 2020

@author: steffens
"""

import sys
import binascii


# Bloco Conversao de ASCII para binario e vice versa, retirado de : https://vike.io/pt/534905/


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

#FIM bloco Conversao de ASCII para binario e vice versa, retirado de : https://vike.io/pt/534905/




cripto=''
param = sys.argv[1:]  # entrada de parametros

if len(param)==1:  # Testa se a quantidade de parametros é correta
    arqTextoClaro = param[0]


else:
    print('Quantidade de parametros invalida! \n Passe o arquivo que gerará o resumo criptográfico.\n')
    print('Exemplo: $ python trab3.py lucas.txt  \n ou\n  $ python3 trab3.py lucas.txt  ')
    exit()


#Abrir o arquivo de texto claro
with open(arqTextoClaro, 'r') as f:
    texto = f.read() # Le arquivo

lista=[]
i=0 # Auxilar percorerr o texto a ser cifrado
j=0
vetor =''
while (i < len(texto)-1):

    if(j<=8):
        vetor+=texto[i] # Cria uma string com os caracteres
        j=j+1
        if(j==8): # Se j=8 os 8 caracteres foram formados e podem ser adicionados a lista

                vetor = text_to_bits(vetor)
                lista.append(vetor)
                vetor=''
                j=0
    i+=1

if(j>0): # Se percorreu os caracteres e nao formou blocos completos pega oque sobrou e coloca 1 ate bater no numero de bits escolhidos
    vetor = text_to_bits(vetor)
    while len(vetor)<64:
                vetor+='1'
    lista.append(vetor)
#print('Lista com vetores')
#print(lista)
lista2=[]
p=0
while (p <= len(lista)-1):  # Enquanto todos os blocos nao forem percorridos
        x= list(lista[p]) # Lista e separa os bits de cada bloco
    #    print('Original:')
    #    print(x)
        j=0 #Variavel auxiliar para tamanho do vetor de um bloco
        k=0  #Variavel auxiliar para controlar a n rotação a esquerda
        while(j<=len(x)-1):
            if(k<=p):
                aux=x[0]
                del(x[0])
                x.append(aux)
                k+=1

            j+=1
    #    print('\n\n\ - Rotacionado:')
        #print(x)
        lista2.append(x)
       # print('\n\n\n')
        p+=1
#print('\n\n\n')
#print(list(lista2))
#print('\n\n\n')
#print(list(lista2[0]))

t=[]
p=0
# Bloco que faz o xor consecutivo
#print(len(lista2))

while (p <= len(lista2)-1):  # Enquanto todos os blocos nao forem percorridos

    if(len(lista2)==1):
        print('Texto não possui mais de um bloco de 64 bits, para aplicar o XOR, a entrada rotacionada e em hexadecimal é: ')
        string=''
        string=string.join(list(lista2[0]))
        print(hex(int(string, 2)))
        exit()

    elif(p==0):
        x= list(lista2[p]) # Lista e separa os bits de cada bloco
        y= list(lista2[p+1])

        o = 0
        while(o <= len(x)-1):
            if(y[o]==x[o]):

                cripto+='0'

            else:
                cripto+='1'


            o+=1
        t.append(cripto)
        y.clear()

        y = list(t[0])
        t.clear()


        cripto=''
        p+=2


    else:
        x= list(lista[p]) # Lista e separa os bits de cada bloco

        o = 0
        while(o <= len(x)-1):
            if(y[o]==x[o]):
                cripto+='0'
            else:
                cripto+='1'

            o+=1
        t.append(cripto)
        y.clear()
        y = list(t[0])
        t.clear()


        cripto=''
        p+=1

#print(y)
#print(len(y))

string=''
string=string.join(y)
print('Para ver os blocos rotacionados basta descomentar as linhas:79,80,91 e 92.')
print('Saida em Binario:')
print(string)
print('\n')
print('Saida em hexadecimal')
print(hex(int(string, 2)))
