#!/usr/bin/env python
# coding: utf-8

# Atividade 4
# ==========
# 
# 1 Menor de dois pares: Escreva uma função que retorne o menor de dois números
# dados se ambos os números forem pares, mas retorna o maior se um dos dois for
# ímpar. Exemplo:
# menor_de_dois_pares(2,4) --&gt; 2
# menor_de_dois_inpares (2,5) --&gt; 5

# In[2]:


def menor(numero1,numero2):
    if numero1 % 2 == 0 and numero2 % 2 == 0:
        if numero1 < numero2:
            return numero1
        else:
            return numero2
    else:
        if numero1 > numero2:
            return numero1
        else:
            return numero2
            
print(menor(2,4))
print(menor(4,3))


# 2 Mesma letra: Escreva uma função que receba uma string com duas palavras e
# retorne True se ambas palavras começarem com a mesma letra. Exemplo:
# mesma_letra(&#39;Cão covarde&#39;) -&gt; True
# mesma_letra(&#39;Vira Lata&#39;) -&gt; False

# In[1]:


def primeira_letra(arg):
    palavras = arg.title().split()
    if palavras[0][0] == palavras[1][0]:
        return True
    else:
        return False
    
print (primeira_letra('Joao Victor Campos'))
print (primeira_letra('Campeao'))


# 3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as
# palavras na ordem reversa. Exemplo:
# mestre_yoda(&#39;Eu estou em casa&#39;) --&gt; &#39;casa em estou Eu&#39;
# mestre_yoda(&#39;Estamos prontos&#39;) --&gt; &#39;prontos Estamos&#39;

# In[14]:


frase = 'Estamos prontos'
string =''
for palavra in frase.split(" "):
    string += palavra[::-1]+" "

print(invertida)


# 4 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver
# em alguma posição da lista um 3 do lado de outro 3. Exemplo:
# tem_33([1,3,3]) --&gt; True
# tem_33([1,3,1,3]) --&gt; False
# tem_33([3,1,3]) --&gt; False

# In[17]:


def tem33(arg):
    tem3 = False
    for i in arg:
        if i == 3:
            if tem3 is True:
                return True
            else:
                tem3 = True
        else:
            tem3 = False
    else:
        return False
    
print (tem33([1,3,3]))
print (tem33([3,1,3]))
print (tem33([1,3,1,3]))
print (tem33([1,3,1,3,3]))


# 5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for
# menor que 21, retorne o valor da soma. Se for maior do que 21 e houver um 11,
# subtraia 10 da soma antes de apresentar o resultado. Se o valor da soma passar de
# 21, retorne ‘ESTOUROU’. Exemplo:
# 
# blackjack(5,6,7) --&gt; 18
# blackjack(9,9,9) --&gt; &#39;ESTOUROU&#39;
# blackjack(9,9,11) --&gt; 19

# In[33]:


def soma(num1,num2,num3):
    total= num1 + num2 + num3
    
    if total <= 21:
        print(total)
    else: 
        if num1 == 11 or num2 == 11 or num3 == 11:
            total = total - 10
            print(total)
        else:
            print(total, 'ESTOUROU' )
            

soma(10,8,10)
soma(1,8,7)
soma(11,11,8)


# 6 Espião: Escreva uma função que receba uma lista de
# inteiros e retorne True se contém um 007 em ordem, mesmo
# que não contínuo. Exemplo:
# espiao([1,2,4,0,0,7,5]) --&gt; True
# espiao([1,0,2,4,0,5,7]) --&gt; True
# espiao([1,7,2,4,0,5,0]) --&gt; False

# In[36]:


def espiao(arg):
    z1 = False
    z2 = False
    s = False
    for i in arg:
        if i == 0:
            if s is False:
                if z1 is False and z2 is False:
                    z1 = True
                elif z1 is True and z2 is False:
                    z2 = True
                else:
                    return False
            else:
                return False
        elif i == 7:
            if z1 is True and z2 is True:
                return True
            else:
                return False
            
print (espiao([1,2,5,0,0,7,9]))
print (espiao([2,7,3,4,0,5,0]))
print (espiao([4,0,2,4,0,5,8]))
print (espiao([6,7,3,4,0,7,0,7]))


# In[ ]:




