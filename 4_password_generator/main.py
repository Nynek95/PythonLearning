import random
import string


def f_walidacja(a, b, arg1=""):
    while True:
        try:
            zmienna = int(input("Twój wybór: "))
            if a <= zmienna <= b:
                return zmienna
            else:
                print(f"Wybrałeś liczbę spoza zakresu ({a}, {b}), spróbuj raz jeszcze.\n")
                print(arg1)
        except ValueError:
            print("Wprowadzasz jakiś dziwny znak głuptasie, spróbuj raz jeszcze.\n")
            print(arg1)
            continue


def f_pobranie_wartosci(a, b, arg1=""):
    while True:
        print(arg1)
        wartosc = f_walidacja(a, b, arg1)
        return wartosc


# delkaracja zmiennych
haslo_lista = []
n = -1

# program
print("\nWitaj w generatorze haseł!\n")
while n != 2:
    print("[1] - Generuj hasło napisanym algorytmem\n[2] - Wyjdź\n")
    n = f_walidacja(1, 2, "[1] - Generuj hasło\n[2] - Wyjdź\n")
    if n == 1:
        dlugosc_hasla = f_pobranie_wartosci(8, 50, "Jak długie ma być hasło? (min. 8 znaków, max. 50 znaków): ")
        print()
        male_litery = f_pobranie_wartosci(1, dlugosc_hasla,
                                          f"Ile małych liter ma mieć hasło? (min. 1, max. {dlugosc_hasla}) :")
        dost_znaki = dlugosc_hasla - male_litery
        print()
        duze_litery = f_pobranie_wartosci(1, dost_znaki,
                                          f"Ile duzych liter ma mieć hasło? (min. 1, max. {dost_znaki}) :")
        dost_znaki -= duze_litery
        print()
        znaki_specjalne = f_pobranie_wartosci(1, dost_znaki,
                                              f"Ile znaków specjalnych ma mieć hasło? (min. 1, max. {dost_znaki}) :")
        dost_znaki -= znaki_specjalne
        print()
        cyfry = f_pobranie_wartosci(1, dost_znaki, f"Ile cyfr ma mieć hasło? (min. 1, max. {dost_znaki}) :")
        dost_znaki -= cyfry
        if dost_znaki > 0:
            print(f"\nPozostało {dost_znaki} znaków do wykorzystania, więc program zastąpił je małymi literami.")
            male_litery += dost_znaki
        print("\nPodsumowanie:")
        print("Małe litery:", male_litery)
        print("Duże litery:", duze_litery)
        print("Znaki specjalne:", znaki_specjalne)
        print("Cyfry:", cyfry, "\n")

        # generowanie hasła
        for _ in range(dlugosc_hasla):
            if male_litery > 0:
                haslo_lista.append(random.choice(string.ascii_lowercase))
                male_litery -= 1
            if duze_litery > 0:
                haslo_lista.append(random.choice(string.ascii_uppercase))
                duze_litery -= 1
            if znaki_specjalne > 0:
                haslo_lista.append(random.choice(string.punctuation))
                znaki_specjalne -= 1
            if cyfry > 0:
                haslo_lista.append(random.choice(string.digits))
                cyfry -= 1
        random.shuffle(haslo_lista)
        print("Wygenerowane hasło:", "".join(haslo_lista), "\n")

print("\nMam nadzieje, że program Ci się przydał, już nikt nie złamie Twojego hasła!\nProgram stworzył Maciek.")
