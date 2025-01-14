# Program obliczający sumę cyfr liczby

def suma_cyfr(liczba):
    suma = 0
    for cyfra in str(liczba):
        if cyfra.isdigit():  # Sprawdzamy, czy znak jest cyfrą
            suma += int(cyfra)
    return suma

# Pobieranie liczby od użytkownika
liczba = input("Podaj liczbę: ")

# Obliczanie sumy cyfr
wynik = suma_cyfr(liczba)

# Wyświetlanie wyniku
print(f"Suma cyfr liczby {liczba} wynosi: {wynik}")
