import random

def moja(x):
    a = 0
    b = 1
    while a < x:
        b,a = a + b,b
        print(a)
    return x
#moja(100)


def moja2():
    lista = []
    lista.append(1)
    lista.append(5)
    lista.append(6)
    lista.append(1)
    print(lista)
    print(lista.count(1))
    return
#moja2()


ileliczb = int(input("Podaj ilosć typowanych liczb: "))
maksliczba = int(input("Podaj z ilu liczb: "))
i = 0
while i < ileliczb:
    liczba = random.randint(1,maksliczba)
    liczby = []
    if liczby.count(liczba)==0:
        liczby.append(liczba)
    i = i + 1
print ("Wylosowane liczby", liczby)
        