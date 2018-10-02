import random

ileliczb = int(input("Podaj ilosć typowanych liczb: "))
maksliczba = int(input("Podaj z ilu liczb: "))
i = 0
liczby = []
while i < ileliczb:
    liczba = random.randint(1,maksliczba)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
    i = i + 1
print ("Wylosowane liczby", liczby)
        