##tutaj definiujemy funkcje
def f_zla_liczba():
    print("Wybrałeś niepoprawną liczbę, spróbuj ponownie")
    print()
def f_pokaz_zad():
    index_zad = 0
    if len(lista_zadan) == 0:
        print("Lista zadań jest pusta\n")
    else:
        print("Oto Twoja lista zadań:")
        for zadanie in lista_zadan:
            print(zadanie + " ["+str(index_zad)+"]")
            index_zad += 1
        print()
def f_dodaj_zad():
    lista_zadan.append(input("Wpisz nowe zadanie: "))
    print("Dodano zadanie\n")
def f_usun_zad():
    try:
        index_zad = int(input("Podaj indeks zadania do usuniecia: "))
    except ValueError:
        print("Dlaczego wpisujesz literę zamiast liczby?\n")
        return
    if index_zad < 0 or index_zad > (len(lista_zadan)-1):
        print("Zadanie o podanym numerze nie istnieje\n")
        return
    print("Usunięto zadanie: " + lista_zadan.pop(index_zad)+"\n")
def f_czysc_zad():
    lista_zadan.clear()
    print("Wyczyszczono listę\n")
def f_zapis_do_pliku():
    plik = open("zadania.txt", "w+")
    for zadanie in lista_zadan:
        plik.write(zadanie + "\n")
    plik.close()
    print("Zadanie zostało zapisane do pliku zadania.txt\n")
def f_odczyt_z_pliku():
    try:
        plik = open("zadania.txt")
        for linia in plik.readlines():
            lista_zadan.append(linia.strip())
        plik.close()
    except FileNotFoundError:
        return
def f_domyslna_lista():
    lista_zadan.clear()
    lista_zadan.append("Wstań z łóżka")
    lista_zadan.append("Umyj zęby")
    lista_zadan.append("Weź prysznic")
    lista_zadan.append("Wstaw wodę na herbatę")
    print("Wygenerowano domyślną listę zadań\n")
def f_zmien_kolejnosc():
    f_pokaz_zad()
    try:
        index1 = int(input("Wprowadź indeks zadania, które chcesz zmienić?: "))
        if index1 < 0 or index1 > len(lista_zadan) - 1:
            print("Zadanie o takim indeksie nie istnieje\n")
            return
        print("Wybrałeś zadanie o nazwie: " + lista_zadan[index1])
    except ValueError:
        print("Wybrałeś złą wartość, spróbuj raz jeszcze\n")
        return
    try:
        index2 = int(input("Wprowadź nowy indeks zadania: "))
        if index2 < 0 or index2 > len(lista_zadan) - 1:
            print("Zadanie o takim indeksie nie istnieje\n")
            return
        print("Wybrałeś zadanie o nazwie: " + lista_zadan[index2])
    except ValueError:
        print("Wybrałeś złą wartość, spróbuj raz jeszcze\n")
        return
    zmienna_pom1 = lista_zadan[index1]
    zmienna_pom2 = lista_zadan[index2]
    lista_zadan.insert(index1, zmienna_pom2)
    lista_zadan.pop(index1 + 1)
    lista_zadan.insert(index2, zmienna_pom1)
    lista_zadan.pop(index2 + 1)

    print("Zadania '" + zmienna_pom2 + "' oraz '" + zmienna_pom1 + "' zostały pomyślnie zamienione kolejnością\n")
def f_oznacz_wykonane():
    f_pokaz_zad()
    try:
        index1 = int(input("Wprowadź indeks zadania, które chcesz oznaczyć jako wykonane: "))
        if index1 < 0 or index1 > len(lista_zadan) - 1:
            print("Zadanie o takim indeksie nie istnieje\n")
            return
    except ValueError:
        print("Wybrałeś złą wartość, spróbuj raz jeszcze\n")
        return
    zmienna_pom1 = lista_zadan[index1]
    if zmienna_pom1.find("WYKONANE") > 0:
        print("Kolego, nie można oznaczyć powtórnie wykonanego zadania jako wykonane.\n")
    else:
        zmienna_pom2 = zmienna_pom1 + " - WYKONANE"
        lista_zadan.insert(index1, zmienna_pom2)
        lista_zadan.pop(index1 + 1)
        print("Oznaczyłeś jako wykonane zadanie: " + zmienna_pom1 + "\n")

##deklaracja zmiennej przed wejściem do pętli
n1 = -1
n2 = -1
lista_zadan = []
f_odczyt_z_pliku()
print("To jest pierwszy program Maćka\nProszę o wyrozumialość\n")
print("Co chcesz zrobić, wybierz numer (1-9)")

while n1 != 9:
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Czyść liste zadań")
    print("5. Generuj domyślną listę zadań")
    print("6. Zapisz zmiany do pliku")
    print("7. Zmiana indeksów zadania")
    print("8. Oznacz wykonanane zadanie")
    print("9. Wyjdź \n")
    ##Wykluczenie wpisania błędnej zmiennej
    try:
        ##nie zapominać o konwersji do int
        n1 = int(input("Wybierz numer (1-9): "))
    except ValueError:
        print("Wybrałeś złą wartość, wprowadź raz jeszcze\n")
        continue
    if n1 > 9 or n1 < 1:
        f_zla_liczba()
    if n1 == 1:
        f_pokaz_zad()
    if n1 == 2:
        f_dodaj_zad()
    if n1 == 3:
        f_usun_zad()
    if n1 == 4:
        f_czysc_zad()
    if n1 == 5:
        f_domyslna_lista()
    if n1 == 6:
        f_zapis_do_pliku()
    if n1 == 7:
        f_zmien_kolejnosc()
    if n1 == 8:
        f_oznacz_wykonane()

while n2 != 2:
    print("Czy chcesz przed wyjściem z programu zapisać listę zadań do pliku?\n")
    try:
        ##nie zapominać o konwersji do int
        n2 = int(input("1. Tak\n2. Nie\nWybierz numer (1-2): "))
    except ValueError:
        print("Wybrałeś złą wartość, wprowadź raz jeszcze\n")
        continue
    if n2 > 2 or n1 < 1:
        f_zla_liczba()
    if n2 == 1:
        f_zapis_do_pliku()
        break

print("Wyszedłeś z programu, mam nadzieje, że jeszcze kiedyś tu wrócisz ;)")
