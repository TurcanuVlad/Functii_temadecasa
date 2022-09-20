import math
a=int(input('Dati a='))
b=int(input('Dati b='))
def sum(x,y):
    s=x+y
    return s
print('Suma:', sum(a,b))
def prod(x,y):
    p=x*y
    return p
print('Produsul=', prod(a,b))
def med_aritm(x,y):
    ma=(x+y)/2
    return ma
print('Media aritmetica=', med_aritm(a,b))
def cmmdc(x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x
print('Cel mai mare divizor comun=', cmmdc(a,b))
print('Cel mai mic multiplu comun=', a*b//cmmdc(a,b))
def maxnr(x,y):
    maxim=max(x,y)
    return maxim
def minnr(x,y):
    minim=min(x,y)
    return minim
print('Numarul minim=', minnr(a,b))
print('Numarul maxim=', maxnr(a,b))
def sumaaa():
    s=a+b
    return s
print('Suma fara de x, y:', sumaaa())
def produuus():
    p=a*b
    return p
print('Produs fara de x, y', produuus())
def divizorii(x,y):
    ldiv=[]
    for i in range(1, min(x,y)+1):
        if x%i==y%i==0:
            ldiv.append(i)
    return ldiv
print('Divizorii comuni:', divizorii(a,b))
def fivemult():
    lmult=[]
    for i in range(1,6):
        lmult.append(i*a*b)
    return lmult
print('5 multipli:', fivemult())
def aaaa(x,y):
    interauto=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) in str(y):
            interauto+=str(i)+" "
    return interauto
print('Intersectia:',aaaa(a,b))    
def ppapap(x,y):
    fara_nume=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) not in str(y):
            fara_nume+=str(i)+" "
    return fara_nume
print('A/B:',ppapap(a,b))      
def fafafafa(x,y):
    divx=0
    divy=0
    for i in range(1,x+1):
        if x%i==0 :
            divx+=1
    for i in range(1,y+1):
        if y%i==0 :
            divy+=1   
    if divx==divy:
        sudya="Друзья"  
    else:
        sudya="Враги"  
    return sudya
print(fafafafa(a,b))   