from functools import reduce

def optymalizacja_proceduralna(zadania):
    zadania.sort(key=lambda x: x[0])
    calkowity_czas_oczekiwania = 0
    czas_aktualny = 0
    for czas, nagroda in zadania:
        calkowity_czas_oczekiwania += czas_aktualny
        czas_aktualny += czas
    return zadania, calkowity_czas_oczekiwania

def optymalizacja_funkcyjna(zadania):
    zadania = sorted(zadania, key=lambda x: x[0])
    czasy_oczekiwania = list(map(lambda i: sum(map(lambda z: z[0], zadania[:i])), range(len(zadania))))
    calkowity_czas_oczekiwania = reduce(lambda acc, x: acc + x, czasy_oczekiwania)
    return zadania, calkowity_czas_oczekiwania

zadania = [(3, 100), (1, 200), (2, 150)]

kolejnosc_proceduralna, czas_oczekiwania_proceduralna = optymalizacja_proceduralna(zadania.copy())
print("Kolejność proceduralna:", kolejnosc_proceduralna)
print("Całkowity czas oczekiwania (proceduralne):", czas_oczekiwania_proceduralna)

kolejnosc_funkcyjna, czas_oczekiwania_funkcyjna = optymalizacja_funkcyjna(zadania.copy())
print("Kolejność funkcyjna:", kolejnosc_funkcyjna)
print("Całkowity czas oczekiwania (funkcyjne):", czas_oczekiwania_funkcyjna)
