

'''

EXERCÍCIO 37


def somaI(a):
    if not len(a) == 1:
        return a[0][0] + somaI(a[1:])
    else: return a[-1][0]


def somaF(a):
    if not len(a) == 1:
        return a[0][-1] + somaF(a[1:])
    else: return a[-1][-1]

def excluiI(a):
    if not len(a) == 0:
        a[0].pop(0)
        return excluiI(a[1:])
    else: return 
    
def excluiF(a):
    if not len(a) == 0:
        a[0].pop(-1)
        return excluiF(a[1:])
    else: return 
        
def func(a):   
    if not len(a[0]) == 1:
        if somaI(a) > somaF(a):
            excluiF(a)
            return func(a) + 0
        else:
            excluiI(a)
            return func(a) + 1
    else: return 0
    
a = [[1, 2, 3], [11, 11, 11], [6, 7, 8], [10, 11, 0]]
func(a)


-------------------------------------------------------------------------------



codigo que retorna o indice da lista de lista (linha) que possou a maior soma 
dos valores internos

def soma(a):
    if not len(a) == 0:
        return a[0] + soma(a[1:])
    else: return 0
    

def func(a):   
    if not len(a) == 1:
        if soma(a[0]) > soma(a[-1]):
            return func(a[:-1]) + 0
        else: 
            return func(a[1:]) + 1
    else: return 0
    
a = [[1,2,3],[11,11,11],[6,7,8],[0,0,0]]
func(a)
    

-------------------------------------------------------------------------------

EXERCÍCIO COMPLEMENTAR 6

def aux(a):
  return((aux(a[1:]) if a[0] <= a[1] else 0) if not len(a) == 1 else 1)
def fun(a):
  return(aux(a[0]) + fun(a[1:]) if not len(a) == 0 else 0)
    
a = [[2,2,3,0],[1,2,5,6],[2,4,4]]
fun(a)



-------------------------------------------------------------------------------

EXERCÍCIO COMPLEMENTAR 5


def aux(a):
 return((1 + aux(a[1:]) if a[0] > 0 else -1 + aux(a[1:])) if not len(a) == 0 else 0 )
        
def fun(a):
 return((fun(a[:1]) if aux(a[0]) == 0 else False) if not len(a) == 0 else True)
        
    
    
a = [[2,1,-1,1],[-1,1,-1,1]]
fun(a)

-------------------------------------------------------------------------------

EXERCÍCIO COMPLEMENTAR 4

def aux(a):
    if not len(a) == 0:
        if a[0] == 0:
            a.pop(0)
            return 1 + aux(a) 
        else: a.pop(0); return aux(a)
    else: return 0
    
def fun(a):
    if not len(a) == 0:
        if (len(a[0]) / 2) < aux(a[0]) :
            a.pop(0)
            return fun(a)
        else: return False
    else: return True
    
a = [[2,0,0,0],[0],[0,0,8]]
fun(a)


EXERCÍCIO COMPLEMENTAR 4 versão 2


def aux(a):
 return((1 + aux(a[1:]) if a[0] == 0 else aux(a[1:])) if not len(a) == 0 else 0)
           
def fun(a):
 return((fun(a[1:]) if (len(a[0]) / 2) < aux(a[0]) else False) if len(a) == 0 else True)
           
a = [[2,0,0,0],[0],[0,0,8]]
fun(a)



-------------------------------------------------------------------------------

EXERCÍCIO COMPLEMENTAR 3

def aux(a):
    if not len(a) == 0:
        
        if a[0] % 2 == 0:
            a.pop(0)
            return 1 + aux(a) 
        else: a.pop(0); return aux(a)
        
        return((aux(a[1:]) + 1 if a[0] % 2 == 0 else   ))
        
    else: return 0
    
 

def fun(a):
    if not len(a) == 0:
        if (len(a[0]) / 2) > aux(a[0]) :
            a.pop(0)
            return fun(a)
        else: return True
    else: return False
    
a = [[2,5,3,-1],[3],[8,6,5]]
fun(a)




-------------------------------------------------------------------------------
EXERCÍCIO COMPLEMENTAR 2

def aux(a):
    if not len(a) == 0:
        if a[0] >= 0:
            a.pop(0)
            return aux(a)
        else: return False
    else: return True
    
    
def fun(a):
    if not len(a) == 0:
        if aux(a[0]) == True:
            a.pop(0)
            return fun(a)
        else: return False
    else: return True
    
a = [[2,4,3,-1],[3],[],[8,0,6]]
fun(a)

-------------------------------------------------------------------------------

    EXERCÍCIO COMPLEMENTAR 1

def aux(s):
    if not len(s) == 0:
        if s[0] % 2 == 0:
            s.pop(0)
            return 1 + aux(s)
        else: s.pop(0); return aux(s)
    else: return 0

def fun(a):
    if not len(a) == 0:
       return aux(a[0]) + fun(a[1:])
    else: return 0

a =   [[2,4,3,1],[3,5,7],[],[8,0,6]]
fun(a)
        
        

-------------------------------------------------------------------------------

EXERCÍCIO 36

NÃO É POSSÍVEL UM INPUT TYPE LISTA RETORNAR LISTA DE LISTA POR RECURSÃO
SEM AS LISTAS DE LISTAS JÁ SEREM ADICIONADAS. OU SEJA, É IMPOSSÍVEL PELA 
LIMITAÇÃO DE OPRAÇÕES DE LISTAS DESSE EXERCÍCIO SER DO TIPO DE RECURSÃO DE 'VOLTA'

RECURSÃO DE IDA:
    AQUELA QUE É LINEAR E SÓ MUDA O VALOR DA VARIÁVEL

RECURSÃO DE VOLTA:
    AQUELA QUE IRÁ EFETUAR OPERAÇÕES QUANDO O RETORNO CHEGAR

(O TIPO DESSE EXERCÍCIO É O DE IDA)


def aux(a):
    a.insert(0,[])
    a.insert(0,[])
    return a
    
def separa(a):   
    
 if not len(a) == 2:
        
   if type(a[0]) == list:
            
     if a[2] % 3 == 0 and a[2] % 5 == 0:
                a[0].append(a[2])
                a[1].append(a[2])
                a.pop(2)
                return separa(a)
            
     elif a[2] % 3 == 0:
                 a[0].append(a[2])
                 a.pop(2)
                 return separa(a)
           
     elif a[2] % 5 == 0:
                 a[1].append(a[2])
                 a.pop(2)
                 return separa(a)
             
     else: a.pop(2); return separa(a)
                  
   else: a = aux(a); return separa(a)
                       
 else: return a    
       
           
a = [1,2,3,4,5,9,15]  
separa(a)  




-------------------------------------------------------------------------------

 EXERCÍCIO 38

 def multp(a,n):
   
   c = (2 ** n)
   
   c = str(c)
    
   if not int(c[0]) == a:
       
       return 1 + multp(a , n + 1) 
   
   else: 
        return 0
   

def potencia(k):
    
    return multp(k,0)
    
        
        
potencia(3)




-------------------------------------------------------------------------------


EXERCÍCIO  35



import math
  

def primoQ(a):

    if a == 1:
        return False

    for i in range(2, int(math.sqrt(a)+1)):

        if a % i == 0:
            return False
    
    return True 

def primos1(a):
    
    g = []
    
    if not len(a) == 0:
        
        if primoQ(a[-1]):
            g = [a.index(a[-1])]
            a.pop(-1)
            return g + primos1(a)
        
        else:
            a.pop(-1)
            return primos1(a)    
        
    else:    
         return g
          

def indPrimos1(a):
    
 g = []

 if not len(a) == 0:
     
     g = [primos1(a[0])]
     
     a.pop(0)
     
     return  g + indPrimos1(a)
    
 else: return g
             

a = [[1,2,3], [3,4,5], [7,6,4]]

indPrimos1(a)




-------------------------------------------------------------------------------


TRANSFORMANDO NUMEROS INTEIROS EM ELEMENTOS DE LISTA

def aux(a):
    
    g = []
    
    a = str(a)
    
    if not len(a) == 1:
        
        g.extend([int(a[-1])])
        
        return  aux(a[:-1]) + g
    
    else: return list([int(a[0])])



-------------------------------------------------------------------------------



Retornar em uma lista de lista, os numeros primos de uma lista de lista


import math
  

def primoQ(a):

    if a == 1:
        return False

    for i in range(2, int(math.sqrt(a)+1)):

        if a % i == 0:
            return False
    
    return True 

def primos1(a):
    
    g = []
    
    if not len(a) == 0:
        
        if primoQ(a[0]):
            g = [a[0]]
            a.pop(0)
            return g + primos1(a)
        
        else:
            a.pop(0)
            return primos1(a)    
        
    else:    
         return g
          

def indPrimos1(a):
    
 g = []

 if not len(a) == 0:
     
     g = [primos1(a[0])]
     
     a.pop(0)
     
     return  g + indPrimos1(a)
    
 else: return g
             

a = [[1,2,3], [3,4,5], [7,6,4]]

indPrimos1(a)





-------------------------------------------------------------------------------

Exercício 39


def repete(a):
    
    g = []
   
    if not len(a) == 0:
        
        if a.count(a[len(a) - 1]) <= len(a):
                      
            
            g += [a[len(a) - 1]]
            
            g *= (len(a))
            
            a.pop(len(a) - 1)
            
            return  repete(a) + g
        
        else: 
            
            a.pop(len(a) - 1)
            
            return repete(a)
        
        
    else: return g
    
    
a = [1,1,2,3]

repete(a)





-------------------------------------------------------------------------------




Função que retorna em uma lista, todos os numeros primos de uma lista de lista



def primoQ(a,b):
    
    if a == b:
       
       return primoQ(a, b - 1)
   
    if a == 1 or a == 0:
        
        return False
    
    if not b < 2:
        
        if  a % b == 0:
         
             return False
      
        else:
        
             return primoQ(a,b-1)
         
    else:
        
          return True

def indPrimos1(a):
    
  g = []

  if not len(a[0]) == 0:  

    if not primoQ(a[0][0], a[0][0]) == True :
        
        a[0].pop(0)
        
        return indPrimos1(a) 
    
    else: 
        
        g += [a[0][0]]
        
        a[0].pop(0)
        
        return g + indPrimos1(a)
    
  else: 
       
        if len(a) == 1:
            
            return g
        
        else:
            
            a.pop(0)
       
            return g + indPrimos1(a)
        

a = [[1,2,3], [3,4,5], [7,6,4]]

indPrimos1(a)




------------------------------------------------------------------------------


Exercício 34



def intercala(a,b):
    
    g = []
    
    if not len(b) == 0:
    
        g += [a[0]]
        
        g += [b[0]]
        
        return g + intercala(a[1:],b[1:])
    
    else: return g
    
    

a = [4,4,4]

b = [3,2,]

intercala(a,b)



------------------------------------------------------------------------------



Exercício 33



def permutacao(a,b):
      
   a.sort()
   b.sort()
   
   if not len(a) != len(b):
     
      if not len(b) == 0 :
          
                if a[0] == b[0]:  
                 
                  return permutacao(a[1:],b[1:])
              
                else: return False
        
      else: return True
      
   else: return False
       
       
a = [1,2,3]

b = [3,2,1]

permutacao(a,b)




------------------------------------------------------------------------------



Exercício 32




def sup_lista2(a):
    
        g = []
     
        if not len(a[0]) == 1:
            
            
            if a[0][0] > a[0][len(a[0]) - 1]:
                
                a[0] = a[0][:len(a[0]) - 1]
                
                return sup_lista2(a)
            
            else: 
                
                a[0]= a[0][1:]
                
                return sup_lista2(a)
            
        else:   
            
            if len(a) == 1:
                
                return a[0]
            
            else:
            
             g += a[0]
             
             a.pop(0)
 
             return g + sup_lista2(a)
        

    

a = [[1,2,9],[56,3,4],[2,7,8,1]]

sup_lista2(a)





------------------------------------------------------------------------------


Exercício 31




def sup_lista1(a):
     
        if not len(a[0]) == 1:
            
            
            if a[0][0] > a[0][len(a[0]) - 1]:
                
                a[0] = a[0][:len(a[0]) - 1]
                
                return sup_lista1(a)
            
            else: 
                
                a[0]= a[0][1:]
                
                return sup_lista1(a)
            
        else:   
            
            if len(a) == 1:
                
                return a[0][0]
            
            else:
            
             a[0] = a[0] + a[1]
             
             a.pop(1)
        
             return sup_lista1(a)
        

    

a = [[1,2,9],[2,3,4],[2,7,8,1]]

sup_lista1(a)





------------------------------------------------------------------------------


Exercício 30





def lista_igualQ(a,b):
    
    
    if not len(a) == 0 :
    
      if a[0] == b[0] and len(a) == len(b):
          
          return lista_igualQ(a[1:], b[1:])
      
        
      else:
          
          return False
      
    else: 
          return True
          
      


a = [5,3,9]

b = [5,3,8]


lista_igualQ(a,b)





------------------------------------------------------------------------------




Exercício 29



def invertLista(a):
    
    g = []
    
    if not len(a) == 0:
        
        g += [a[0]]
        
        return invertLista(a[1:]) + g
    
    else:
         
        return g
    
    

    
        
    
    
a = [1,2,1,4,1,3,8]
invertLista(a)
    
    
    
    
    

------------------------------------------------------------------------------






Exercício 28



def primoQ(a,b):
    
    if a == b:
       
       return primoQ(a, b - 1)
   
    if a == 1 or a == 0:
        
        return False
    
    if not b < 2:
        
        if  a % b == 0:
         
             return False
      
        else:
        
             return primoQ(a,b-1)
         
    else:
        
          return True

def temPrimoQ(a):
    
  g = []

  if not len(a[0]) == 0:  

    if not primoQ(a[0][0], a[0][0]) == True :
        
        a[0].pop(0)
        
        return temPrimoQ(a) 
    
    else: 
        
        return True
    
  else: 
       
        if len(a) == 1:
            
            return False
        
        else:
            
            a.pop(0)
       
            return temPrimoQ(a)
        

a = [[4,4],[4,6,4]]

temPrimoQ(a)







------------------------------------------------------------------------------

Exercício 27




def sufixoQ(a,b):
    
   if not len(a) == 0:
       
       if a[len(a) - 1] == b[len(b) - 1]:
           
           
           return sufixoQ(a[:len(a) - 1],b[:len(b) - 1])
       
       else:
           
           return False
       
   else: 
        
        return True
    



a = [5,3,8]

b = [1,2,1,4,1,3,8]

sufixoQ(a,b)







-------------------------------------------------------------------------------




Exercício 26


def suc(x):
    
    return x+1

def mapeia(suc,a):
    
    g = []
    
    if not len(a) == 0:
        
        g += [ suc(a[0])  ]
        
        return g + mapeia(suc, a[1:])
    
    else:
        
        return g
            
            
    
a = [1,2,1,4,1,3,8]

mapeia(suc,a)





-------------------------------------------------------------------------------




Exercício 25





def primoQ(a,b):
    
    if not b <= 1:
        
        if  a % b == 0:
         
             return False
      
        else:
        
             return primoQ(a,b-1)
         
    else:
        
          return True
    
    
    
      
def seleccao(a , primoQ):
    
    g = []
    
    if not len(a) == 0:
        
        if primoQ(a[0], a[0] - 1) == True:
            
            g += [a[0]]
            
            return g + seleccao(a[1:], primoQ)
        
        else: 
            
             return seleccao(a[1:], primoQ)
         
    else:
        
         return a




a = [1,2,1,4,1,3,8]
seleccao(a,primoQ)


-------------------------------------------------------------------------------



Exercício 24





def apaga1(a):
    
    g = []
    
    if not len(a[0]) == 0:
        
        if a[1] == a[0][0]:
            
            a[0].pop(0)
                      
            return apaga1(a)
        
        else:
            
            g += [a[0][0]]
            
            a[0] = a[0][1:]
            
            return g + apaga1(a)
        
    else: 
        
        return g



a = [[1,2,1,4,1,9,8], 1]
apaga1(a)





-------------------------------------------------------------------------------




Exercício 23



def apaga(a):
    
   g = []
    
   if  a[1] == a[0][0]:
            
            a[0].pop(0)
                              
            return a[0]
        
   else:
       
       g += [a[0][0]]
       
       a[0] = a[0][1:]
       
       return g + apaga(a)
        
  


a = [[3,2,1,4,1,9,8], 1]
apaga(a)





-------------------------------------------------------------------------------




Exercício 22



def car_pares(a):
    
    g = []
    
    if not len(a) == 0:
        
        if a[0] % 2 == 0:
            
            g += [True]
            
            return g + car_pares(a[1:])
        
        else: 
            
            g += [False]
            
            return g + car_pares(a[1:])
        
    else:
        
        return g
    




a = [1,2,1,4,6]
car_pares(a)






-------------------------------------------------------------------------------




Exercício 21





def pos_max(a):
    

    
    if not len(a) == 0:
        
        if a[0] == a[ len(a) - 1]:
            
            
            return  pos_max(a[:len(a) - 1]) + 1
        
        else:
            
            return pos_max(a[:len(a) - 1])
    else:
        
         return 0
        


a = [1,2,1,4,1]
pos_max(a)






-------------------------------------------------------------------------------





Exercício 20






def lposicoes(a):
    
    
    g = []
    
    if not len(a[0]) == 0:
        
        if a[1] == a[0][len(a[0]) - 1]:
            
            g += [len(a[0]) - 1]
            
            a[0] = a[0][:len(a[0]) - 1]
            
            return  lposicoes(a) + g
        
        else:
            
            a[0] = a[0][:len(a[0]) - 1]
            
            return lposicoes(a)       
        
    else:
        
         return g
        


a = [[1,2,1,4,1], 1]
lposicoes(a)









-------------------------------------------------------------------------------




Exercício 19



def conta(a):
    
    if not len(a[0]) == 0:
        
        if a[1] == a[0][0]:
            
            a[0] = a[0][1:]
            
            return 1 + conta(a)
        
        else:
            
            a[0] = a[0][1:]
            
            return conta(a)       
        
    else:
        
         return 0
        


a = [[1,2,1,4,1], 1]
conta(a)






-------------------------------------------------------------------------------



Exercício 18





from math import inf

def supremo(a):
    
    g = []
    
    if len(a) == 0:
        
        return -inf
    
    if  not len(a) == 1:
        
        if a[0] > a[len(a) - 1]:
        
             g += [a[0]]
            
             return  supremo(a[:len(a) - 1]) 
        
        else:  
            
             g += [a[len(a) - 1]]
            
             return supremo(a[1:])
         
    else:      
            return a[0]
   


a = []  
supremo(a)



-------------------------------------------------------------------------------






Exercício 17



def retira_negativos(a):
    
    g = []
    
    if not len(a) == 0:
        
        if a[0] < 0:
            
            return retira_negativos(a[1:])
        
        else:
            
            g += [a[0]]
            
            return g + retira_negativos(a[1:])
        
    else:
        
        return a
        
    


a = [1,2,-3,-4,-5,6]  
retira_negativos(a)





-------------------------------------------------------------------------------





Exercício 16




def indices_par(a):

     g = []    

     if not len(a) == 0:
         
         if not a[0] % 2 == 0:
             
               return indices_par(a[1:])   
            
         else:
               g = g + [a[0]]
               
               return  g + indices_par(a[1:])   
           
     else:
           return g
         
        

a = [1,2,3,4,5,6]  
indices_par(a) 



-------------------------------------------------------------------------------





Exercício 15



def indices_impar(a):

     g = []    

     if not len(a) == 0:
         
         if a[0] % 2 == 0:
             
               return indices_impar(a[1:])   
            
         else:
               g = g + [a[0]]
               
               return  g + indices_impar(a[1:])   
           
     else:
           return g
         
         



a = [1,2]  
indices_impar(a) 






-------------------------------------------------------------------------------





Exercício 14





def negpos(a):
    
    if not len(a) == 0:
        
        if a[0] < 0:
            
            return -1 + negpos(a[1:])
        
        else:
            
            return 1 + negpos(a[1:])
        
    else:
         
        return 0
    
    
    
    
    
    
    
a = [1,2,3,-1,-2,5,-7]    
negpos(a)







-------------------------------------------------------------------------------




Exercício 13


def pertenceQ(a):
    
 if not a[1] == a[0][0]:
        
    if len(a[0]) == 1:
            
      return False
    
    else:
        
       a[0] = a[0][1:]
    
    return pertenceQ(a)
    
 else:
      return True
    
        
        

a = [[9,0,6] , 1]
    
pertenceQ(a)






-------------------------------------------------------------------------------


Exercício 12


def Todos_impares(a):
    
    
    
    if not a[0] % 2 == 0:
        
        if len(a) == 1:
            
            return True
        
        return Todos_impares(a[1:])
        
    else:
        return False


a = [1,7,3,5]
Todos_impares(a)




-------------------------------------------------------------------------------

Exercício 11



def contem_parQ(a):
    
    
    
    if not a[0] % 2 == 0:
        
        if len(a) == 1:
            
            return False
        
        return contem_parQ(a[1:])
        
    else:
        return True


a = [1,7,3,5]
contem_parQ(a)





-------------------------------------------------------------------------------
Exercício 10


def prod_list(a):
    
    if not len(a) == 1:
        
        return (a[0]) * (prod_list(a[1:]))
        
    else:
        return a[0]


a = [1,2,3,4]
prod_list(a)





-------------------------------------------------------------------------------

Exercício 9 
 
def div(a):
    
    l = []

    if not a == 0:
          
        l += [a**2]   
        
        return l + div(a-1)
    
    else:
        return l
    
    
a = 6
div(a)        
    


-------------------------------------------------------------------------------


Exercício 8 
 
def div(a):
    
    l = []

    if not a == 0:
          
        l += [a**2]   
        
        return  div(a-1) + l
    
    else:
        return l
    
    
a = 6
div(a)        
    

-------------------------------------------------------------------------------


Exercício 6


def num_it(a):
    
 if not a == 1:
    
     if a % 2 == 0:
        
           return 1 + num_it(a/2)
    
     else: 
           return 1 + num_it(3*a + 1)
       
 else:
           return 0
            

num_it(21)



-------------------------------------------------------------------------------
Exercício 5


def aux(a,b):
    
  if not b == 1:
      
      if a % b == 0 :
          
            return b + aux(a,b-1)
      
      else: 
            return aux(a, b - 1)
  
  else:
         return 1
       
       


def num_perf(a):
    
    
   if a == aux(a, a - 1):
       
       return True
   else:
       return False
              
a = 8
num_perf(a)
    





-------------------------------------------------------------------------------


EXERCÍCIO 4


def media_digitos(a):               
    
    a = str(a)
    
   
    
    if not len(a) == 1:
     
        n = len(a)
                                                  
        return (int(a[0]) + (n-1) * media_digitos(a[1:]))/n
        
      
    else:
        
         return int(a) 
        


a = 123
media_digitos(a)


-------------------------------------------------------------------------------





 Programa de soma dos alarismos de um número



def som_digitos(a):
    
    a = str(a)
    
    if not len(a) == 1:
     
        
     return  int(a[len(a) - 1]) + som_digitos(a[:-1])
        
      
    else:
         return int(a[len(a) - 1])
        
 
    
        
a = 293    
som_digitos(a)
        
        
        
k = 345
k = str(k)
k[len(k) - 1]
j = int(k[len(k) - 1])
        



-------------------------------------------------------------------------------




 Exercício 3



def prim_alg(a):
    
  

  a = str(a)
  

  if not len(a) == 1:
            
      
      return prim_alg(a[:-1])     

  
  else: 
      
      
      return a[len(a) - 1]
     
     
a = 678

prim_alg(a)

 
    
 
-------------------------------------------------------------------------------
 Exercício 2
 
def div(a,b):

 if not a == 0:
  
     
   return 1 + div(a-b,b) 

 else:
       return 0
    
a=5
b=7
div(a,b) 


-------------------------------------------------------------------------------


   Soma Mesmo valor n vezes

def somaMV(a,b):
    
   print(a)
    
   if not b == 0:
       
       return a + somaMV(a , b-1) 
   
   else: 
        return 0
   
b=5
a = 2
somaMV(a,b)


-------------------------------------------------------------------------------

   Exercício 1

def nat(a):
    print(a)
  
    if a == 0:
        return 0 
    else:
        return a + nat(a-1)
       
a = 3

nat(a)'''