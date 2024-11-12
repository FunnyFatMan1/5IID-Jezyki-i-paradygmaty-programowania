from functools import reduce

def harmonogram_proceduralny(zadania):
    zadania.sort(key=lambda x: x[1])
    wybrane_zadania = []
    max_nagroda = 0
    czas_zakonczenia_poprzedniego = 0
    for zadanie in zadania:
        if zadanie[0] >= czas_zakonczenia_poprzedniego:
            wybrane_zadania.append(zadanie)
            max_nagroda += zadanie[2]
            czas_zakonczenia_poprzedniego = zadanie[1]
    return max_nagroda, wybrane_zadania

def harmonogram_funkcyjny(zadania):
    zadania = sorted(zadania, key=lambda x: x[1])
    def wybierz_zadania(wybrane, zadanie):
        if not wybrane or zadanie[0] >= wybrane[-1][1]:
            return wybrane + [zadanie]
        return wybrane
    wybrane_zadania = reduce(wybierz_zadania, zadania, [])
    max_nagroda = sum(map(lambda x: x[2], wybrane_zadania))
    return max_nagroda, wybrane_zadania

zadania = [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60)]
max_nagroda_procedural, harmonogram_procedural = harmonogram_proceduralny(zadania)
print("Maksymalna nagroda (proceduralne):", max_nagroda_procedural)
print("Wybrane zadania (proceduralne):", harmonogram_procedural)
max_nagroda_funkcyjna, harmonogram_funkcyjny = harmonogram_funkcyjny(zadania)
print("Maksymalna nagroda (funkcyjne):", max_nagroda_funkcyjna)
print("Wybrane zadania (funkcyjne):", harmonogram_funkcyjny)
