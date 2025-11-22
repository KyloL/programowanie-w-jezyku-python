def iven(liczba) -> bool:
    return (liczba % 2) == 0

l=input("Podaj liczbę: ")

if not iven(int(l)):
    print(str(l) + ' jest liczbą nieparzystą')
else:
    print(str(l) + ' jest liczbą parzystą')