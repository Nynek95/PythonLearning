import sys
import random

glowne_menu = -1
poziom_trudnosci = -1
kategoria = -1
kategoria_imie = -1
lista_hasel = []
uzyte_hasla = []

def f_print(tekst):
    print(tekst)
def f_walidacja(zmienna, a, b, f_print, arg1=""):
    while True:
        try:
            zmienna = int(input("Twój wybór: "))
            if zmienna >= a and zmienna <= b:
                return zmienna
            else:
                print("Wybrałeś liczbę spoza zakresu, spróbuj raz jeszcze.\n")
                f_print(arg1)
        except ValueError:
            print("Wprowadzasz jakiś dziwny znak głuptasie, spróbuj raz jeszcze.\n")
            f_print(arg1)
            continue
def f_losowanko():
    zmienna = random.randint(0, len(lista_hasel)-1)
    return(lista_hasel.pop(zmienna).lower())
def f_odczyt_z_pliku(nazwa_kategorii):
    global lista_hasel
    global uzyte_hasla
    try:
        plik = open(nazwa_kategorii+".txt", encoding="utf8")
        for linia in plik.readlines():
            lista_hasel.append(linia.strip())
        plik.close()
        for x in uzyte_hasla:
            try:
                lista_hasel.remove(str(x).title())
                print('Pomyślnie usunięto hasło "', (str(x).title()) + '" z listy dostępnych haseł')
            except ValueError:
                continue
    except FileNotFoundError:
        return
def f_kreskowanie():
    for lit in slowo:
        if lit == " ":
            slowo_zagadka.append("SPACJA")
        else:
            slowo_zagadka.append("_")
def f_znajdz_indeksy(slowo, litera):
    indeksy = []
    for index, literka_w_slowie in enumerate(slowo):
        if litera == literka_w_slowie:
            indeksy.append(index)
    return indeksy
def f_jeszcze_raz():
    global zmienna_pom
    global glowne_menu
    print("Czy chcesz spróbować jeszcze raz?\n[1] - Tak\n[2] - Nie")
    zmienna_pom = f_walidacja(zmienna_pom, 1, 2, f_print, "No chcesz grać, czy nie?\n[1] - Tak\n[2] - Nie")
    if zmienna_pom == 1:
        print("\nNo to gramy raz jeszcze!\n")
        glowne_menu = 1
    if zmienna_pom == 2:
        print("\nDzięki za gre, mam nadzieje, że dobrze się bawiłeś!\nProgram stworzył Maciek")
        sys.exit(0)

#program
print('\n***Gra "Wisielec"***\n')
    #główne menu
while True:
    if len(uzyte_hasla) > 0:
        print("Oto lista użytych haseł, które się nie powtórzą:", uzyte_hasla, "\n")
    slowo_zagadka = []
    uzyte_litery = []
    lista_hasel = []
    zmienna_pom = -1
    if glowne_menu != 1:
        print('Menu główne\n[1] - Nowa gra\n[2] - Wyjście z programu\n')
        glowne_menu = f_walidacja(glowne_menu, 1, 2, f_print, "Menu główne\n[1] - Nowa gra\n[2] - Wyjście z programu\n")
    if glowne_menu == 1:
        #wybór poziomu trudności
        print("Wybierz poziom trudności:\n[1] - Łatwy (8 szans)\n[2] - Średni (5 szans)\n[3] - Trudny (3 szanse)\n[4] - Powrót do menu głównego\n")
        poziom_trudnosci = f_walidacja(poziom_trudnosci, 1, 4, f_print, "Wybierz poprawnie poziom trudności.\n[1] - Łatwy (8 szans)\n[2] - Średni (5 szans)\n[3] - Trudny (3 szanse)\n[4] - Powrót do menu głównego\n")
        if poziom_trudnosci == 1:
            liczba_zyc = 8
        if poziom_trudnosci == 2:
            liczba_zyc = 5
        if poziom_trudnosci == 3:
            liczba_zyc = 3
        if poziom_trudnosci == 4:
            glowne_menu = -1
            continue
        print("Wybrałeś poziom z", liczba_zyc, "szansami\n")
        #wybór kategorii
        print("Wybierz numer kategorii hasła:\n[1] - Imiona\n[2] - Państwa\n[3] - Zwierzęta\n[4] - Powrót do menu głównego\n")
        kategoria = f_walidacja(kategoria, 1, 4, f_print, "Wybierz poprawny numer kategorii hasła.\n[1] - Imiona\n[2] - Państwa\n[3] - Zwierzęta\n[4] - Powrót do menu głównego\n")
        if kategoria == 1:
            #wybór kategorii imienia
            print("Jakie imię chcesz zgadywać?\n[1] - Żeńskie\n[2] - Męskie\n[3] - Powrót do menu głównego\n")
            kategoria_imie = f_walidacja(kategoria_imie, 1, 3, f_print, "Wybierz poprawnie kategorię imienia\n[1] - Żeńskie\n[2] - Męskie\n[3] - Powrót do menu głównego\n")
            if kategoria_imie == 1:
                print("Wybrałeś kategorię z imionami żeńskimi. Zabawa start!\n")
                nazwa_kategorii = "imiona_zenskie"
                f_odczyt_z_pliku(nazwa_kategorii)
                slowo = (f_losowanko())
            if kategoria_imie == 2:
                print("Wybrałeś kategorię z imionami męskimi. Zabawa start!\n")
                nazwa_kategorii = "imiona_meskie"
                f_odczyt_z_pliku(nazwa_kategorii)
                slowo = (f_losowanko())
            if kategoria_imie == 3:
                glowne_menu = -1
                continue
        if kategoria == 2:
            print("Wybrałeś kategorię z nazwami państw. Zabawa start!\n")
            nazwa_kategorii = "panstwa"
            f_odczyt_z_pliku(nazwa_kategorii)
            slowo = (f_losowanko())
        if kategoria == 3:
            print("Wybrałeś kategorię ze zwierzętami. Zabawa start!\n")
            nazwa_kategorii = "zwierzeta"
            f_odczyt_z_pliku(nazwa_kategorii)
            slowo = (f_losowanko())
        if kategoria == 4:
            glowne_menu = -1
            continue
        #kreskowanie hasła
        f_kreskowanie()
        ###cheat
        #print("podpowiedź", slowo)
        ###cheat
        #odgadywanie hasła
        while zmienna_pom == -1:
            print("Oto zgadywane hasło:", slowo_zagadka, "\nZostało Ci " + str(liczba_zyc) + " szans\n")
            litera = input("Podaj literę: ").lower()
            if len(litera) == 0:
                print("Dlaczego nie wpisujesz żadnego znaku gamoniu?\nWprowadź proszę tym razem pojedynczą literę.\n")
            if len(litera) > 0 and litera.isalnum() == False and litera.isalpha() == False and litera.isdigit() == False and litera.islower() == False:
                print("Wprowadziłeś znak specjalny zamiast literki gamoniu!\nWprowadź proszę tym razem poprawną literę.\n")
            if litera.isalnum() == True and litera.isalpha() == False and litera.isdigit() == True and litera.islower() == False:
                print("Wprowadziłeś liczbę zamiast literki gamoniu!\nWprowadź proszę tym razem poprawną literę.\n")
            if litera.isalnum() == True and litera.isalpha() == True and litera.isdigit() == False and litera.islower() == True:
                if litera in uzyte_litery:
                    print("Podałeś poraz kolejny tę samą literę gamoniu!\nWprowadź proszę tym razem poprawną literę.\n")
                    continue
                if len(litera) > 1:
                    print("Dlaczego podajesz więcej niż jedną literę\nWprowadź proszę tym razem pojedynczą literę.\n")
                    continue
                uzyte_litery.append(litera)
                print("Oto lista użytych liter: " + str(uzyte_litery))
                znalezione_indeksy = f_znajdz_indeksy(slowo, litera)
                if len(znalezione_indeksy) == 0:
                    print("Niestety, nie ma takiej litery")
                    liczba_zyc -= 1
                    if liczba_zyc == 0:
                        print("Hasło brzmiało: " + slowo.title() + "\nPrzegrałeś, spróbuj ponownie. Następnym razem będzie lepiej!\n")
                        uzyte_hasla.append(slowo)
                        f_jeszcze_raz()
                else:
                    for index in znalezione_indeksy:
                        slowo_zagadka[index] = litera
                        print("Brawo, odgadłeś literę!")
                        if slowo_zagadka.count("_") == 0:
                            print('Brawo Ty, odgadłeś hasło i wygrałeś czajnik!\nOdgadnięte hasło to "' + slowo.title() + '"\n')
                            uzyte_hasla.append(slowo)
                            f_jeszcze_raz()
    if glowne_menu == 2:
        break

print("\nDzięki za gre, mam nadzieje, że dobrze się bawiłeś!\nProgram napisał Maciek")
