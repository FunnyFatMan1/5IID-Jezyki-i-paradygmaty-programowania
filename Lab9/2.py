import functools

lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

liczby_parzyste = list(filter(lambda x: x % 2 == 0, lista_liczb))

suma_parzystych = functools.reduce(lambda acc, x: acc + x, liczby_parzyste, 0)

print(f"Liczby parzyste: {liczby_parzyste}")
print(f"Suma liczb parzystych: {suma_parzystych}")
