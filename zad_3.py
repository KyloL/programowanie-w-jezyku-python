def iven(liczba) -> bool:
    return (liczba % 2) == 0


L = input("Podaj liczbę: ")

if not iven(int(L)):
    print(str(L) + ' jest liczbą nieparzystą')
else:
    print(str(L) + ' jest liczbą parzystą')
