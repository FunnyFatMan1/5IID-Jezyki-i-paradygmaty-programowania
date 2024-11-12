def podziel_paczki(wagi, max_waga):

    if any(waga > max_waga for waga in wagi):
        przekroczone_paczki = [waga for waga in wagi if waga > max_waga]
        raise ValueError(f"Paczki o wagach {przekroczone_paczki} przekraczają maksymalną dozwoloną wagę {max_waga} kg")

    wagi = sorted(wagi, reverse=True)
    kursy = []

    for waga in wagi:
        for kurs in kursy:
            if sum(kurs) + waga <= max_waga:
                kurs.append(waga)
                break
        else:
            kursy.append([waga])

    return len(kursy), kursy

wagi = [10, 15, 7, 20, 5, 8, 10]
max_waga = 25

liczba_kursow, kursy = podziel_paczki(wagi, max_waga)

for i, kurs in enumerate(kursy, 1):
    print(f'Kurs {i}: {kurs} - suma wag: {sum(kurs)} kg.')
