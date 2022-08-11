#sortowoanie bąbelkowe, czyli wymyślanie koła na nowo
#czy jest ono wolniejsze niż metoda sort() dla listy?
#przy okazji sprawdzisz zdolności obliczeniowe Twojego komputera

import random
import datetime

def f_walidacja(a, b, arg1 = ""):
    while True:
        try:
            zmienna = int(input("Twój wybór: "))
            if zmienna >= a and zmienna <= b:
                return zmienna
            else:
                print("Wybrałeś liczbę spoza zakresu, spróbuj raz jeszcze.\n")
                print(arg1)
        except ValueError:
            print("Wprowadzasz jakiś dziwny znak głuptasie, spróbuj raz jeszcze.\n")
            print(arg1)
            continue
def wyg_listy():
    global lista_liczb
    while True:
        try:
            a = int(input("\nIle elementów ma zawierać Twoja lista?: "))
            if a > 1:
                break
            if a == 0 or a == 1:
                print(f"Nie uważasz, że wpisanie wartości {a} jest bez sensu?")
            else:
                print("Nie wpisuj liczb ujemnych!")
        except ValueError:
            print("Wprowadzasz jakiś dziwny znak głuptasie, spróbuj raz jeszcze.\n")
            continue
    while True:
        try:
            b = int(input("Podaj górną wartość zakresu losowania liczb lub wpisz 0, jeśli zakres ma być taki sam jak liczba elementów: "))
            if b >= 1:
                break
            if b == 0:
                b = a
                break
            else:
                print("Nie wpisuj liczb ujemnych!\n")
        except ValueError:
            print("Wprowadzasz jakiś dziwny znak głuptasie, spróbuj raz jeszcze.\n")
            continue
    lista_liczb = []
    for c in range(0, a):
        lista_liczb.append(random.randint(0, b))
    return lista_liczb
def sort_bomb(lista):
    dl_listy = len(lista)
    while dl_listy > 1:
        zamien = False
        for a in range(0, dl_listy - 1):
            if lista[a] > lista[a+1]:
                lista[a], lista[a + 1] = lista[a + 1], lista[a]
                zamien = True
        dl_listy -= 1
        if zamien == False:
            break
    return lista

n = 0
print("\nAlgorytm sortowania bąbelkowego")
while n != 3:
    print("\n[1] - Bąbelkujemy napisanym algorytmem\n[2] - Sortujemy gotową funkcją sort()\n[3] - Koniec programu\n")
    n = f_walidacja(1, 3, "[1] - Bąbelkujemy napisanym algorytmem\n[2] - Sortujemy gotową funkcją sort()\n[3] - Koniec programu\n")
    if n == 1:
        czas_przed = datetime.datetime.now()
        print(f'\nOto lista liczb przed bąbelkowaniem: {wyg_listy()}\nLista powyżej to liczby przed bąbelkowaniem.\n')
        print(f'Oto lista liczb po bąbelkowaniu: {sort_bomb(lista_liczb)}\nLista powyżej to liczby po bąbelkowaniu.')
        czas_po = datetime.datetime.now()
        print(f'\nCzas obliczeń dla metody bąbelkowania wynosi: {czas_po - czas_przed}')
    if n == 2:
        lista_liczb_sort = wyg_listy()
        czas_przed = datetime.datetime.now()
        print(f'\nOto lista liczb przed sortowaniem: {lista_liczb_sort}\nLista powyżej to liczby przed sortowaniem.\n')
        lista_liczb_sort.sort()
        czas_po = datetime.datetime.now()
        print(f'Oto lista liczb po sortowaniu: {lista_liczb_sort}\nLista powyżej to liczby po sortowaniu.')
        print(f'\nCzas obliczeń dla metody sortowania wynosi: {czas_po - czas_przed}')
    if n == 3:
        break
print("Mam nadzieje, że Twój komputer jest szybszy niż mój! Maciek.")
